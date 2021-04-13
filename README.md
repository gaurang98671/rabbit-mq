# rabbit-mq
## Commands

### Pull docker image of rabbitMQ
>docker pull rabbitmq
### Run container and map ports
>docker run -d --name rabbit-mq-server -p 5672:5672 rabbitmq
### Run sender.py
>python sender.py
### Run receiver.py
>python receiver.py

## Work queues 
Uses round ribbon to disrtubute messages accross all consumers

![](https://www.rabbitmq.com/img/tutorials/python-two.png)

## Fanout
Uses pub-sub approach to send each message to all subscribed comsumers

![](https://www.rabbitmq.com/img/tutorials/python-three-overall.png)

## Selective routing
Uses routing key to distrubute message

![](https://www.rabbitmq.com/img/tutorials/python-four.png)

## Pattern routing
Distrubutes messages based on routing key's pattern

![](https://www.rabbitmq.com/img/tutorials/python-five.png)

## RPC
RPC protocol using rabbitMQ

![](https://www.rabbitmq.com/img/tutorials/python-six.png)


