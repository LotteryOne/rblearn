import pika, time

rqhost = 'cloudfun.org'
mycd = pika.PlainCredentials(username='admin', password='admin@123')
conn = pika.BlockingConnection(pika.ConnectionParameters(rqhost, 5672, '/', credentials=mycd))

channel = conn.channel()
channel.queue_declare(queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep(body.decode('utf-8').count('.'))
    print(" [x] done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
