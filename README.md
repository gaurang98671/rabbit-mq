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

## Fanout
Uses pub-sub approach to send each message to all subscribed comsumers

## Direct routing 
Uses routing key to distrubute message

## Selective routing
Distrubutes messages based on routing key's pattern


