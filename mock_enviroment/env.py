import os

os.environ['PROJECT_DIR'] = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------KAFKA-----------------------------------
os.environ['TITLE_TOPIC'] = 'titles'
os.environ['FEATURES_TOPIC'] = 'features'
os.environ['KAFKA_SERVER'] = 'localhost:9092'
os.environ['KAFKA_OFFSET'] = 'earliest'

# -------------------------------------TEST-------------------------------------
os.environ['TEST_TITLES'] = os.getenv('PROJECT_DIR') + '/test_data/titles.json'
os.environ['TEST_FEATURES'] = os.getenv('PROJECT_DIR') + '/test_data/features.json'
