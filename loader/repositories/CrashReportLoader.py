from src import config
from .BaseLoader import BaseLoader
import psycopg2



class CrashReportLoader(BaseLoader):

    def __init__(self, queue):
        super(CrashReportLoader, self).__init__(queue)

    def save(self, event):
        pass