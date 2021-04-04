import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
#channel.exchange_declare(exchange='logs', exchange_type='fanout')

a=True
while(a):
    message= str(input("Enter message: "))
    if(message=="kill yourself"):
        a=False
    else:

        channel.basic_publish(exchange='logs', routing_key='', body=message)
        print("Message send: ", message)


connection.close()