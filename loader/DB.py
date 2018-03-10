import psycopg2



def get_db():
    conn = psycopg2.connect(
        "dbname='assessment' user='iugo' host='localhost' password='postgres'")

    curs = conn.cursor()
    return conn, curs