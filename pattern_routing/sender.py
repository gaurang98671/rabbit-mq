import pika
import sys
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='topic')

keys = sys.argv[1:]

a = True
while a:
    message = str(input("Enter message: "))

    if message == "kill yourself":
        a = False
    else:

       for key in keys:
           channel.basic_publish(exchange='direct_logs', routing_key=key, body=message)
           print("Message send: ", message)


connection.close()