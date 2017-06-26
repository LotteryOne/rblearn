from util import conn

connection = conn.getConnection("/")
channel = connection.channel()
# fanout
result = channel.exchange_declare(exchange='topic_log', type='topic')
print(result)

serverity = 'xml.json'
message = "send " + serverity + " message"

channel.basic_publish(exchange='topic_log', routing_key=serverity, body=message)

connection.close()
