import pika
from os import environ

username = environ.get('RABBIT_USERNAME', 'rabbitmq')
password = environ.get('RABBIT_PASSWORD', 'rabbitmq')
host = environ.get('RABBIT_HOST', 'localhost')

def _create_queue(name):
    credentials = pika.PlainCredentials(
        username=username, password=password)
    parameters = pika.ConnectionParameters(
        credentials=credentials, host=host)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    # channel.queue_declare(
    #     queue=name, durable=True, auto_delete=False, exclusive=False)
    return connection, channel


_crash_report_queue = _create_queue('crash_report')

queues = {
    # 'crash_report': _crash_report_queue,
    'crash_report': _create_queue('crash_report'),
    'purchase': _create_queue('purchase'),
    'install': _create_queue('install')
}