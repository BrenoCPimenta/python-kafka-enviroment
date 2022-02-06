import json
import os
from config import env
from kafka import KafkaConsumer
from kafka import KafkaProducer
from features.features_manager import load_features
from scraper.title_scraper import TitleScraper


def serializer(message):
    """
    Serialize messages as JSON
    """
    return json.dumps(message).encode('utf-8')


def main() -> None:
    """Listen to kafka topics and produce features from URLs"""
    # Read env variables
    kafka_server = os.environ.get('KAFKA_SERVER')
    kafka_offset = os.environ.get('KAFKA_OFFSET')
    topic_features = os.environ.get('FEATURES_TOPIC')
    topic_urls = os.environ.get('URL_TOPIC')
    # Kafka Producer
    producer = KafkaProducer(
        bootstrap_servers=[kafka_server],
        value_serializer=serializer
    )
    # Kafka Consumer
    consumer = KafkaConsumer(
        topic_urls,
        bootstrap_servers=kafka_server,
        auto_offset_reset=kafka_offset
    )
    cnt = 0
    scraper = TitleScraper(15)
    for url in consumer:
        cnt += 1
        title = scraper.get_title(url.value)
        features = load_features(title, url)
        print(cnt, ' - intermediate:\n', json.loads(features), '\n\n')
        producer.send(topic_features, json.loads(features))


if __name__ == '__main__':
    main()
