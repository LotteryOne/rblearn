from util import conn

connection = conn.getConnection("/")
channel = connection.channel()
# fanout
result = channel.exchange_declare(exchange='logs', type='fanout')
print(result)

message = "send message"
channel.basic_publish(exchange='logs', routing_key='', body=message)

connection.close()
