import pika
import uuid


class FactorialRpcClient:

    def __init__(self):
        self.corr_id = str(uuid.uuid4())
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host="localhost"
            )
        )
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue="", exclusive=True)
        self.call_back_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.call_back_queue,
            on_message_callback=self.on_message,
            auto_ack=True
        )

    def on_message(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.channel.basic_publish(exchange='', routing_key='rpc_server', properties=pika.BasicProperties(
            correlation_id=self.corr_id,
            reply_to=self.call_back_queue
        ),
        body=str(n)
        )

        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)


client = FactorialRpcClient()

print(client.call(3))
