import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost'
    )
)

channel= connection.channel()

channel.queue_declare("rpc_server")

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)

def on_request(ch, method, props, body):
    print("Message received")
    ch.basic_publish(exchange='', routing_key= props.reply_to, properties= pika.BasicProperties(correlation_id= props.correlation_id), body= "Hello message received")
    ch.basic_ack(delivery_tag= method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="rpc_server", on_message_callback= on_request)

print("Listening for messages =>")
channel.start_consuming()
