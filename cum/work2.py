import pika

rqhost = 'cloudfun.org'
mycd = pika.PlainCredentials(username='admin', password='admin@123')
conn = pika.BlockingConnection(pika.ConnectionParameters(rqhost, 5672, '/', credentials=mycd))

channel = conn.channel()
channel.exchange_declare(exchange='logs',type='fanout')

result = channel.queue_declare(exclusive=True)
print(result)

channel.queue_bind(exchange='logs', queue=result.method.queue)

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))


channel.basic_consume(callback,
                      queue=result.method.queue,
                      no_ack=False)

channel.start_consuming()
