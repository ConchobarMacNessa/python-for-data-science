import tweepy
from textblob import TextBlob
# import numpy as np
import csv

execfile("./environment.py")

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.search("brexit")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    value = "negative" if analysis.sentiment.polarity <= 0 else "positive"
    with open("./csv/twitter/test.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([tweet.text.encode("utf-8"), value])
