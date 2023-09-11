import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='1hello')

channel.basic_publish(exchange='',
                      routing_key='1hello',
                      body='another msg')
print(" [x] Sent 'Hello World!'")

channel.queue_declare(queue='1hello')

connection.close()