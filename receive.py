#!/usr/bin/env python
import pika, sys, os

def main():
    
    print("")

    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq-service', port=5672))
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except:
        print ("could not establish connection")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
