import pika, sys

rqhost = 'cloudfun.org'

mycd = pika.PlainCredentials(username='admin', password='admin@123')
conn = pika.BlockingConnection(pika.ConnectionParameters(rqhost, 5672, '/', credentials=mycd))
channel = conn.channel()

# create queue hello
# linux commond : rabbitmq list_queues
channel.queue_declare(queue='hello', durable=True)

message = 'message:'
for a in (1, 5):
    message = message + ':' + '%s' % ('.' * a)
    print('message:', message)
    channel.basic_publish(exchange='', routing_key='hello', body=message)

conn.close()
