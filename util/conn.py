import pika

rqhost = 'cloudfun.org'
mycd = pika.PlainCredentials(username='admin', password='admin@123')


def getConnection(vh):
    return pika.BlockingConnection(pika.ConnectionParameters(host=rqhost, port=5672, virtual_host=vh, credentials=mycd))


def callback(ch, method, properties, body):
    print(" [x] reciver : %s" % (body,))
