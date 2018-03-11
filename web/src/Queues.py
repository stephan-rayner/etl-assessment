import pika
from os import environ
QUEUE_HOST = environ.get('QUEUE_HOST', 'localhost')
QUEUE_USERNAME = environ.get('QUEUE_USERNAME', 'rabbitmq')
QUEUE_PASSWORD = environ.get('QUEUE_PASSWORD', 'rabbitmq')

def get_queue(name):
    credentials = pika.PlainCredentials(
        username='rabbitmq', password='rabbitmq')
    parameters = pika.ConnectionParameters(
        credentials=credentials, host=QUEUE_HOST)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(
        queue=name, durable=True, auto_delete=False, exclusive=False)
    return connection, channel


_crash_report_queue = get_queue('crash_report')

queues = {
    # 'crash_report': _crash_report_queue,
    'crash_report': get_queue('crash_report'),
    'purchase': get_queue('purchase'),
    'install': get_queue('install')
}