import pika

rqhost = 'cloudfun.org'

mycd = pika.PlainCredentials(username='admin', password='admin@123')
conn = pika.BlockingConnection(pika.ConnectionParameters(rqhost, 5672, '/', credentials=mycd))
channel = conn.channel()

# create queue hello
# linux commond : rabbitmq list_queues
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

conn.close()
