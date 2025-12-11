import pika
import os
import time
import sys

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')

def main():
    connection = None
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
            break
        except pika.exceptions.AMQPConnectionError:
            print("Worker menunggu RabbitMQ...")
            time.sleep(5)

    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Menunggu pesan. Tekan CTRL+C untuk keluar')

    def callback(ch, method, properties, body):
        print(f" [x] Diterima: {body.decode()}")
        time.sleep(1)
        print(" [x] Selesai Diproses")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)