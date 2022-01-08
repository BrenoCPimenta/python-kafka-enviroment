import env
import json
import os
import random
import sys
import time
from datetime import datetime
from kafka import KafkaProducer


def serializer(message):
    """
    Serialize messages as JSON
    """
    return json.dumps(message).encode('utf-8')


def read_titles(doc_address) -> list:
    """
    get title data storage
    on json File
    """
    data = []
    with open(doc_address, mode='r') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    for title in data:
        print(data)
    return data


if __name__ == "__main__":
    # Read env variables:
    topic = os.environ.get('TITLE_TOPIC')
    kafka_server = os.environ.get('KAFKA_SERVER')
    titles_file = os.environ.get('TEST_TITLES')
    # Read data
    data = read_titles(titles_file)
    # Kafka Producer
    producer = KafkaProducer(
        bootstrap_servers=[kafka_server],
        value_serializer=serializer
    )
    # Produces data into topic
    cnt = 0
    while True:
        cnt += 1
        if not data:
            sys.exit()
        title = data.pop()
        print(f'{cnt} - Producing title@ {datetime.now()}\n {str(title)} \n')
        producer.send(topic, title)
        # Produces titles in between 2 and 10 seconds
        time_to_sleep = random.randint(2, 10)
        time.sleep(time_to_sleep)
