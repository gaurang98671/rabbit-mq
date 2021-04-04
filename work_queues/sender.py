import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')

a=True
while(a):
    message= str(input("Enter message: "))
    if(message=="kill yourself"):
        a=False
    else:

        channel.basic_publish(exchange='', routing_key='hello', body=message)
        print("Message send: ", message)


connection.close()