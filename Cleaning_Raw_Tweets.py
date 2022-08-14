# Importing required libraries

import warnings
import csv
warnings.filterwarnings("ignore")
import pandas as pd
import re
import emoji
import nltk

nltk.download('words')
words = set(nltk.corpus.words.words())


# Load dataset
def load_data():
    data = pd.read_csv('dataset.csv')
    return data


tweet_df = load_data()

data = pd.read_csv('dataset.csv', index_col=0)
new_data = data.drop_duplicates('tweet_text', keep='first')
new_data["location"].fillna("NA", inplace=True)


# delete the duplicates by dropping them and store the result value to a new variable

def cleaner(tweet: new_data['tweet_text']):
    # for tweet in  new_data['tweet_text']:
    tweet = re.sub("@[A-Za-z0-9]+", "", tweet)
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)
    tweet = tweet.replace(",", "").replace('\\xe2\\x80\\x99s', '')
    tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI)  # Remove Emojis
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI)  # Remove Emojis
    tweet = tweet.replace("_", " ").replace("b", "")  # Remove hashtag sign but keep the text
    return (tweet)


def cleanerUserName(username: new_data['username']):
    username = username.replace("b", "")
    username = username.replace(",", "")
    return username


def cleanLocation(location: new_data['location']):
    location = location.replace(",", "")
    return location

def cleaningHashTags(hashtags: new_data['all_hashtags']):
    hashtags = hashtags.replace(",", "#")
    return hashtags


new_data['tweet_text'] = new_data['tweet_text'].map(lambda x: cleaner(x))
new_data['username'] = new_data['username'].map(lambda x: cleanerUserName(x))
new_data['location'] = new_data['location'].map(lambda x: cleanLocation(x))
new_data['all_hashtags'] = new_data['all_hashtags'].map(lambda x: cleaningHashTags(x))
new_data.to_csv('clean_Data.csv')  # specify location
file = pd.read_csv('clean_Data.csv', header=1, index_col=0)
print(file)
file.to_csv('clean_Data.csv')