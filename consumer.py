from kafka import KafkaConsumer

TOPIC_NAME = 'items'
#bin/kafka-topics.sh --create --partitions 1 --replication-factor 1 --topic items --bootstrap-server localhost:9092

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print(message)
