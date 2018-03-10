import io
import json
import psycopg2
import pandas as pd
import pika

# Connect Queue and stuff
credentials = pika.PlainCredentials(username='rabbitmq', password='rabbitmq')
parameters = pika.ConnectionParameters(
    credentials=credentials, host='localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Connect DB stuff
conn = psycopg2.connect(
    "dbname='assessment' user='iugo' host='localhost' password='postgres'")
curs = conn.cursor()

queue = 'crash_report'

method_frame, _, _ = channel.basic_get(queue)
count = method_frame.message_count

data = io.StringIO()
print(data)
print("PRE Loop Count", count)

for i in range(count):
    method_frame, header_frame, body = channel.basic_get(queue)
    if method_frame:
        print("method_frame", method_frame.message_count)
        print("body", body)
        payload = json.loads(body)
        # data.write('n'.join([payload['user_id'], payload['timestamp'], payload['message']]))
        data.write('\n'.join([
            str(payload['user_id']),
            str(payload['timestamp']), payload['message']
        ]))
        # (header_frame, body)
        channel.basic_ack(method_frame.delivery_tag)
    else:
        print('No message returned')

data.seek(0)
curs.copy_from(data, 'crash_report')

connection.close()

# ####################################
# conn = psycopg2.connect(DSN)
# curs = conn.cursor()

# data = StringIO.StringIO()
# data.write('\n'.join(['1', '2', '3']))
# data.seek(0)

# curs.copy_from(data, 'my_table')