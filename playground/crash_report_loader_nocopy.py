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

data = []
print(data)
print("PRE Loop Count", count)

for i in range(count):
    method_frame, header_frame, body = channel.basic_get(queue)
    if method_frame:
        print("method_frame", method_frame.message_count)
        print("body", body)
        payload = json.loads(body)
        # data.write('n'.join([payload['user_id'], payload['timestamp'], payload['message']]))
        data.append((payload['user_id'], payload['timestamp'],
                     payload['message']))
        # (header_frame, body)
        channel.basic_ack(method_frame.delivery_tag)
    else:
        print('No message returned')


args_str = b','.join(curs.mogrify("(%s,%s,%s)", x) for x in data)
curs.execute(b"INSERT INTO crash_report(user_id, timestamp, message) VALUES " +
             args_str)
conn.commit()
print("ARGS:", args_str)

connection.close()

# ####################################

# args_str = b','.join(cur.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s)", x) for x in tup)


# conn = psycopg2.connect(DSN)
# curs = conn.cursor()

# data = StringIO.StringIO()
# data.write('\n'.join(['1', '2', '3']))
# data.seek(0)

# curs.copy_from(data, 'my_table')