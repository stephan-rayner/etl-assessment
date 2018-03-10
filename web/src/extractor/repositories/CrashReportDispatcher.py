from .CrashReportLoader import CrashReportLoader
from src import config
import pandas as pd

class CrashReportDispatcher(object):
    """ Deals with saving crash reports to the db."""

    def __init__(self):
        super(CrashReportDispatcher, self).__init__()

    def csv_save(self, event):
        csv_dir = '{}crash_reports.csv'.format(config.CSV_DIR)
        try:
            df = pd.read_csv(csv_dir, )
        except:
            df = pd.DataFrame()

        s = pd.Series(event)
        df.append(s, ignore_index=True).to_csv(csv_dir, index=False)

    def save(self, event):
        self.csv_save(event)

    def submit(self, event):
        # submit to correct rabbit queue
        pass