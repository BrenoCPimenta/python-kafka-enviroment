import env
import json
import os

from kafka import KafkaConsumer


if __name__ == "__main__":
    # Env variables:
    kafka_server = os.environ.get('KAFKA_SERVER')
    kafka_offset = os.environ.get('KAFKA_OFFSET')
    topic = os.environ.get('FEATURES_TOPIC')
    features_file = os.environ.get('TEST_FEATURES')
    # Kafka Consumer
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=kafka_server,
        auto_offset_reset=kafka_offset
    )
    for title in consumer:
        with open(features_file, 'a') as file:
            file.write(str(title)+'\n')
