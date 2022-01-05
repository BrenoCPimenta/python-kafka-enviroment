import time
import json
import random
from datetime import datetime
from data_generator import generate_message
from kafka import KafkaProducer


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    cnt = 0
    while True:
        cnt += 1
        # Generate a message
        dummy_message = generate_message()

        # Send it to our 'messages' topic
        #print(f'{cnt} - Producing message @ {datetime.now()} | Message = {str(dummy_message)} \n')
        print(f'{cnt} - Producing message: {str(dummy_message)} \n')
        producer.send('messages1', dummy_message)

        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)
