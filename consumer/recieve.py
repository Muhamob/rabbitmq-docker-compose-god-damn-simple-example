import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue="handshake")


def callback(ch, method, properties, body):
    print("recieved")
    print(f"[X] Recieved {body}")


channel.basic_consume(queue="handshake",
                      auto_ack=True,
                      on_message_callback=callback)

print("Start consuming")
channel.start_consuming()
