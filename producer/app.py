from flask import Flask, request, jsonify
import pika
import os
import time

app = Flask(__name__)
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')

def get_connection():
    while True:
        try:
            conn = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
            return conn
        except pika.exceptions.AMQPConnectionError:
            print("Menunggu RabbitMQ siap...")
            time.sleep(5)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    msg = data.get('message', 'Hello')
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=msg,
        properties=pika.BasicProperties(delivery_mode=2)
    )
    connection.close()
    return jsonify({"status": "Message Sent", "message": msg})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)