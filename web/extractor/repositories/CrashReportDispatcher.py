from .CrashReportLoader import CrashReportLoader
from web import config
import pandas as pd

class CrashReportDispatcher(object):
    """ Deals with saving crash reports to the db."""

    def __init__(self):
        super(CrashReportDispatcher, self).__init__()

    def db_save(self, event):
        loader = CrashReportLoader()
        loader.save(event)

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