import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    result= channel.queue_declare(queue='', exclusive= True)

    channel.queue_bind(exchange='logs', queue= result.method.queue)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

    channel.basic_consume(queue=result.method.queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)