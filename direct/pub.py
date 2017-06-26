from util import conn

connection = conn.getConnection("/")
channel = connection.channel()
# fanout
result = channel.exchange_declare(exchange='level_log', type='direct')
print(result)

serverity = 'error'
message = "send " + serverity + " message"

channel.basic_publish(exchange='level_log', routing_key=serverity, body=message)

connection.close()
