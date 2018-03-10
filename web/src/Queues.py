import pika


def _create_queue(name):
    credentials = pika.PlainCredentials(
        username='rabbitmq', password='rabbitmq')
    parameters = pika.ConnectionParameters(
        credentials=credentials, host='localhost')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(
        queue=name, durable=True, auto_delete=False, exclusive=False)
    return channel


_crash_report_queue = _create_queue('crash_report')

queues = {
    # 'crash_report': _crash_report_queue,
    'crash_report': _create_queue('crash_report'),
    'purchases': None,
    'installs': None
}