import json
import os
import sys
import traceback

#from src.content_features.count_exclamation import count_exclamation
#from src.content_features.count_hashtags import count_hashtags
#from src.content_features.count_uppercase_words import count_uppercase_words
#from src.content_features.LIWC_metrics import LIWC_metrics
#from src.content_features import text_metrics
from features.sentiment_analysis import sample_analyze_sentiment as SentimentAnalyzer
from features.toxicity_threat_insult import toxicity_threat_insult
#from scraper.title_scraper import execute


def load_features(title, url):
    aux = {}
    #toxicity = toxicity_threat_insult(title)
    #aux.update(toxicity)
    sentiment = SentimentAnalyzer(title)
    aux.update(sentiment)
    """
    exclamation = count_exclamation(title)
    aux.update(exclamation)
    uppercase = count_uppercase_words(title)
    aux.update(uppercase)
    hashtags = count_hashtags(title)
    aux.update(hashtags)
    """
    """
    text = text_metrics.run(title)
    aux.update(text)
    LIWC = LIWC_metrics(title)
    aux.update(LIWC)
    """
    return {'title': title, 'url': url, 'content_features': aux}
