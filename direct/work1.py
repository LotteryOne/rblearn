import util.conn as conn

connection = conn.getConnection('/')

channel = connection.channel()

channel.exchange_declare(exchange='level_log', type='direct')

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

serverities = ['info', 'error']

for serverity in serverities:
    channel.queue_bind(exchange='level_log', queue=queue_name, routing_key=serverity)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.basic_consume(conn.callback, queue=queue_name, no_ack=True)

channel.start_consuming()
