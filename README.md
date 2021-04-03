# rabbit-mq

## Pull docker image of rabbitMQ
>docker pull rabbitmq
## Run container
>docker run -d --name rabbit-mq-server -p 5672:5672 rabbitmq
## Run sender.py
>python sender.py
## Run receiver.py
>python receiver.py
