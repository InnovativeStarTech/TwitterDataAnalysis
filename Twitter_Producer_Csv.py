import json
import csv
import tweepy
import re
import io

# Variables that contains the user credentials to access Twitter API
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


def create_dataset(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    # Twitter authentication and the connection to Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Initializing Tweepy API
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Name of csv file to be created
    fname = "dataset"

    # Open the spreadsheet
    with open('%s.csv' % (fname), 'w', encoding="utf-8") as file:
        w = csv.writer(file)

        # Write header row (feature column names of your choice)
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'location',
                    'followers_count', 'retweet_count', 'favorite_count'])

        # For each tweet matching hashtag, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase + ' -filter:retweets', lang="en",
                                   tweet_mode='extended').items(1000):
            w.writerow([tweet.created_at,
                        tweet.full_text.replace('\n', ' ').encode('utf-8'),
                        tweet.user.screen_name.encode('utf-8'),
                        [e['text'] for e in tweet._json['entities']['hashtags']],
                        tweet.user.location,
                        tweet.user.followers_count,
                        tweet.retweet_count,
                        tweet.favorite_count])


# Enter your hashtag here
hashtag_phrase = "#Qualys"

if __name__ == '__main__':
    create_dataset(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)