import Queues
import DB


class BaseLoader(object):
    """docstring for BaseLoader"""

    def __init__(self, queue):
        super(BaseLoader, self).__init__()
        self.queue = queue
        self.connection, self.channel = Queues.queues[queue]
        self.conn, self.curs = DB.get_db()
