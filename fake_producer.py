import env
import json
import os
import random
import sys
import time
from datetime import datetime
from kafka import KafkaProducer


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)


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
    # Env variables:
    topic = os.environ.get('TITLE_TOPIC')
    titles_file = os.environ.get('TEST_TITLES')
    # Read data
    data = read_titles(titles_file)
    # Produces data into topic
    cnt = 0
    while True:
        cnt += 1
        if not data:
            sys.exit()
        title = data.pop()
        print(f'{cnt} - Producing title@ {datetime.now()}\n {str(title)} \n')
        producer.send('messages1', title)
        # Produces titles in between 2 and 10 seconds
        time_to_sleep = random.randint(2, 10)
        time.sleep(time_to_sleep)
