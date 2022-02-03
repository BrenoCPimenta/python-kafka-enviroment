# python-kafka-enviroment


### Mock Enviroment

The idea is to create an environment to produce and consume data via Kafka topics from the docker running application.
For this matter, there are two scripts and two files on the _mock_enviroment/_ folder.
* The first script, _fake_producer.py_ reads the titles from the file _mock_enviroment/test_data/titles.json_ and sends the titles to the broker via the title's topic, so our application can consume this data. In order to represent a real system, there is a random variation between 2 and 10 seconds to send each title.

* The second script, _fake_consumer.py_ consumes batches of records from the broker via the topic of the feature, these records are the processed features from the initial titles, afterward, it saves the data into _mock_enviroment/test_data/features.json_ .

### Execution:

1. Start **KAFKA**
    1.1. Start **Zookeeper** (ONLY IF NEEDED):
    (local use: ```bin/zookeeper-server-start.sh config/zookeeper.properties```)
    1.2 Start **Kafka**:
    (local use: ```bin/kafka-server-start.sh config/server.properties```)
2. Start **Docker** (our application)
3. Start **Mock Enviroment**:
    3.1 Enter folder: ```cd mock_enviroment```
    3.2 Run consumer: ```python3 fake_consumer.py```
    3.3 Run producer: ```python3 fake_producer.py```
