import psycopg2
from web import config


class CrashReportRepo(object):
    """ Deals with saving crash reports to the db."""

    def __init__(self):
        super(CrashReportRepo, self).__init__()

    def save(self, event):
        q = """INSERT INTO crash_report(user_id, timestamp, message)
            VALUES({}, {}, '{}')
        """.format(event['user_id'], event['timestamp'], event['message'])

        conn = psycopg2.connect(config.DB_STRING)
        cur = conn.cursor()
        cur.execute(q)
        conn.commit()