import pika
from os import environ

username = environ.get('QUEUE_USERNAME', 'rabbitmq')
password = environ.get('QUEUE_PASSWORD', 'rabbitmq')
host = environ.get('QUEUE_HOST', 'localhost')


def get_queue(name):
    credentials = pika.PlainCredentials(
        username=username, password=password)
    parameters = pika.ConnectionParameters(
        credentials=credentials, host=host)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(
        queue=name, durable=True, auto_delete=False, exclusive=False)
    return connection, channel

# initiating queues.
queues = {
    'crash_report': _create_queue('crash_report'),
    'purchase': _create_queue('purchase'),
    'install': _create_queue('install')
} 