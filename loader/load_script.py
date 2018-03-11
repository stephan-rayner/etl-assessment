import json
import pika
import Queues
import DB


def unpack_data(channel, queue, mapper):
    print("Loading::{}".format(queue), end=' | ')
    data = []
    # get count
    count = 0
    method_frame, header_frame, body = channel.basic_get(queue)
    if method_frame:
        count = method_frame.message_count
        print("Count:", count + 1)
        payload = json.loads(body)
        data.append(mapper(payload))
        channel.basic_ack(method_frame.delivery_tag)
    else:
        print('No data to unpack')

    for i in range(count):
        method_frame, header_frame, body = channel.basic_get(queue)
        if method_frame:
            payload = json.loads(body)
            data.append(mapper(payload))
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print('No message returned')

    return data

def load_crash_report_events():
    queue = 'crash_report'
    mapper = lambda payload: (payload['user_id'], payload['timestamp'], payload['message'])
    connection, channel = Queues.queues[queue]
    conn, curs = DB.get_db()
    data = unpack_data(channel, queue, mapper)
    args_str = b','.join(curs.mogrify("(%s,%s,%s)", x) for x in data)
    
    if args_str:
        curs.execute(b"INSERT INTO crash_report(user_id, timestamp, message) VALUES " + args_str)
        conn.commit()
    connection.close()


def load_purchase_events():
    queue = 'purchase'
    mapper = lambda payload: (payload['user_id'], payload['timestamp'], payload['sku'])
    connection, channel = Queues.queues[queue]
    conn, curs = DB.get_db()
    data = unpack_data(channel, queue, mapper)
    args_str = b','.join(curs.mogrify("(%s,%s,%s)", x) for x in data)

    if args_str:
        curs.execute(
            b"INSERT INTO purchase(user_id, timestamp, sku) VALUES " +
            args_str)
        conn.commit()

    connection.close()


def load_install_events():
    queue = 'install'
    mapper = lambda payload: ((payload['user_id'], payload['timestamp']))
    connection, channel = Queues.queues[queue]
    conn, curs = DB.get_db()
    data = unpack_data(channel, queue, mapper)
    args_str = b','.join(curs.mogrify("(%s,%s)", x) for x in data)

    if args_str:
        curs.execute(b"INSERT INTO install(user_id, timestamp) VALUES " +
                 args_str)
        conn.commit()

    connection.close()


def main():
    load_crash_report_events()
    load_purchase_events()
    load_install_events()

if __name__ == '__main__':
    main()