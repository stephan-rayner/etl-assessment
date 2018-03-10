import io
import psycopg2
import pandas as pd


def main():
    s_buf = io.StringIO()
    csv_dir = '{}crash_reports.csv'.format("./CSV/")
    df = pd.read_csv(csv_dir)
    df.to_csv(s_buf, index=False)
    conn = psycopg2.connect(
        "dbname='assessment' user='iugo' host='localhost' password='cAgw8Eva'")
    s_buf.seek(0)
    cur = conn.cursor()
    cur.copy_from(s_buf, 'crash_report', sep=',')
    # cur.copy_from(s_buf, 'crash_report')
    # conn.commit()

if __name__ == '__main__':
    main()