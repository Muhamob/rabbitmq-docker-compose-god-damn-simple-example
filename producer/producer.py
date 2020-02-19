import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue="handshake")

data = "Hello world"
channel.basic_publish(exchange="", routing_key="handshake", body=data.encode())
print("[X] Sent")
connection.close()
