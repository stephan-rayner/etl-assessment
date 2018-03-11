import json
import pika
import Queues
import DB


def get_count(channel, queue):
    method_frame, _, _ = channel.basic_get(queue)
    if method_frame:
        return method_frame.message_count
    else:
        return 0


def load_crash_report_events():
    queue = 'crash_report'
    print("Loading::{}".format(queue))

    # Connect Queue and stuff
    connection, channel = Queues.queues[queue]

    # I think this is why we have an off by one.

    count = get_count(channel, queue)
    print("Count:", count)
    data = []

    mapper = lambda payload: (payload['user_id'], payload['timestamp'], payload['message'])

    for i in range(count):
        method_frame, header_frame, body = channel.basic_get(queue)
        if method_frame:
            payload = json.loads(body)
            data.append(mapper(payload))
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print('No message returned')

    # Connect DB stuff
    conn, curs = DB.get_db()

    args_str = b','.join(curs.mogrify("(%s,%s,%s)", x) for x in data)
    if args_str:
        curs.execute(b"INSERT INTO crash_report(user_id, timestamp, message) VALUES " + args_str)
        conn.commit()
    connection.close()


def load_purchase_events():
    queue = 'purchase'
    print("Loading::{}".format(queue))

    # Connect Queue and stuff
    connection, channel = Queues.queues[queue]

    count = get_count(channel, queue)
    print("Count:", count)
    data = []

    mapper = lambda payload: (payload['user_id'], payload['timestamp'], payload['sku'])

    for i in range(count):
        method_frame, header_frame, body = channel.basic_get(queue)
        if method_frame:
            payload = json.loads(body)
            data.append(mapper(payload))
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print('No message returned')

    # Connect DB stuff
    conn, curs = DB.get_db()

    args_str = b','.join(curs.mogrify("(%s,%s,%s)", x) for x in data)

    if args_str:
        curs.execute(
            b"INSERT INTO purchase(user_id, timestamp, sku) VALUES " +
            args_str)
        conn.commit()

    connection.close()


def load_install_events():
    queue = 'install'
    print("Loading::{}".format(queue))

    # Connect Queue and stuff
    connection, channel = Queues.queues[queue]

    count = get_count(channel, queue)
    print("Count:", count)
    data = []

    mapper = lambda payload: ((payload['user_id'], payload['timestamp']))

    for i in range(count):
        method_frame, header_frame, body = channel.basic_get(queue)
        if method_frame:
            payload = json.loads(body)
            data.append(mapper(payload))
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print('No message returned')

    # Connect DB stuff
    conn, curs = DB.get_db()

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