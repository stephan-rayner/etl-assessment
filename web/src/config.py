from os import environ

DB_NAME = environ.get("DB_NAME", 'assessment')
DB_USER = environ.get("DB_USER", 'iugo')
DB_HOST = environ.get("DB_HOST", 'localhost')
DB_PASSWORD = environ.get("DB_PASSWORD", "")

DB_STRING = "dbname='{}' user='{}' host='{}' password='{}'".format(
    DB_NAME, DB_USER, DB_HOST, DB_PASSWORD)
