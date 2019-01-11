import boto3
import json


def init(ACCESS_KEY, SECRET_KEY):
    return boto3.client(service_name='comprehend', region_name="us-west-2", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

def get_entities(client, title):
    return client.detect_entities(Text=title, LanguageCode='en').get('Entities')

def get_key_phrases(client, title):
    return client.detect_key_phrases(Text=title, LanguageCode='en').get('KeyPhrases')

def get_sentiment(client, title):
    sentiment = client.detect_sentiment(Text=title, LanguageCode='en')
    return [sentiment.get('Sentiment').title(), sentiment.get('SentimentScore')]

