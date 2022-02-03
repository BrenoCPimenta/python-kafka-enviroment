import json
import os
import env
from kafka import KafkaConsumer
from kafka import KafkaProducer


def serializer(message):
    """
    Serialize messages as JSON
    """
    return json.dumps(message).encode('utf-8')


if __name__ == '__main__':
    # Read env variables
    kafka_server = os.environ.get('KAFKA_SERVER')
    kafka_offset = os.environ.get('KAFKA_OFFSET')
    topic_features = os.environ.get('FEATURES_TOPIC')
    topic_titles = os.environ.get('TITLE_TOPIC')
    # Kafka Producer
    producer = KafkaProducer(
        bootstrap_servers=[kafka_server],
        value_serializer=serializer
    )
    # Kafka Consumer
    consumer = KafkaConsumer(
        topic_titles,
        bootstrap_servers=kafka_server,
        auto_offset_reset=kafka_offset
    )
    cnt = 0
    for title in consumer:
        cnt += 1
        print(cnt, ' - intermediate:\n', json.loads(title.value), '\n\n')
        producer.send(topic_features, json.loads(title.value))
