import io
import json
import pika

# Connect and stuff
credentials = pika.PlainCredentials(username='rabbitmq', password='rabbitmq')
parameters = pika.ConnectionParameters(
    credentials=credentials, host='localhost')

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

queue = 'crash_report'

method_frame, _, _ = channel.basic_get(queue)
count = method_frame.message_count

data = io.StringIO()

print("PRE Loop Count", count)
for i in range(count):
    method_frame, header_frame, body = channel.basic_get(queue)
    if method_frame:
        print("method_frame", method_frame.message_count)
        print("body", body)
        print("JSON body", json.loads(body))
        # (header_frame, body)
        channel.basic_ack(method_frame.delivery_tag)
    else:
        print('No message returned')

connection.close()


# ####################################
# conn = psycopg2.connect(DSN)
# curs = conn.cursor()

# data = StringIO.StringIO()
# data.write('\n'.join(['1', '2', '3']))
# data.seek(0)

# curs.copy_from(data, 'my_table')