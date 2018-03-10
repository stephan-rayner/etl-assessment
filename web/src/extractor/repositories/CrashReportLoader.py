from src import config
import psycopg2


class CrashReportLoader(object):

    def __init__(self):
        super(CrashReportLoader, self).__init__()

    def save(self, event):
        q = """INSERT INTO crash_report(user_id, timestamp, message)
            VALUES({}, {}, '{}')
        """.format(event['user_id'], event['timestamp'], event['message'])

        conn = psycopg2.connect(config.DB_STRING)
        cur = conn.cursor()
        cur.execute(q)
        conn.commit()