import psycopg2
from os import environ

db_name = environ.get('DB_NAME', 'assessment')
host = environ.get('DB_HOST', 'localhost')
user = environ.get('DB_USER', 'iugo')
password = environ.get('DB_PASSWORD', 'postgres')

db_string = "dbname='{}' user='{}' host='{}' password='{}'".format(
    db_name, user, host, password)


def get_db():
    conn = psycopg2.connect(db_string)
    curs = conn.cursor()
    return conn, curs