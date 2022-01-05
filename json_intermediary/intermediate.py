import json
from kafka import KafkaConsumer
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    cnt = 0
    # Kafka Consumer
    consumer = KafkaConsumer(
        'messages1',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    for message in consumer:
        cnt += 1
        print(cnt, ' - intermediate:\n', json.loads(message.value), '\n\n')
        producer.send('messages2', json.loads(message.value))
