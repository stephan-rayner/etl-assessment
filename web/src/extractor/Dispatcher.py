import json
from src import Queues

class Dispatcher(object):
    """ Deals with sending events to a designated queue"""

    def __init__(self, queue_name):
        super(Dispatcher, self).__init__()
        self.queue_name = queue_name
        self.channel = Queues.queues[queue_name]

    def submit(self, event):
        # submit to rabbit queue
        payload = json.dumps(event)
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=payload)