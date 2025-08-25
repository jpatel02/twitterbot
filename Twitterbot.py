import tweepy
import os
import json
from random import randint

# Define our constant variables
CONSUMER_KEY = '9ezltcrs4EQ2zRew8AExQWCIU'
CONSUMER_SECRET = 'lKo0ZMvP3tfsdFE2Rj4wXlZmolXwjg9Dv2yLTUFDU2lVKfsAhm'
ACCESS_KEY = '1959370119965986816-R0x7LeYrxQ7zXrVJd26XS6p2ZkSDZu'
ACCESS_SECRET = 'co0iavLCQKrgYeguiNl8x1jQm3nWJbtKiu1q9nCHXhr1F'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMT03gEAAAAANJGZr9QZYz90tmTTlpdvjAXxJhQ%3DbMMzAkOrBzCvxJIOaHSVlFg3k8tPXtw0L25zwrFPgRlrPwmJqx'

# Authenticate to Twitter using OAuth 2.0 Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET)




#Post a tweet
tweet = "Hello, world! This is a tweet from Tweepy scheduled at 1pm!"
response = client.create_tweet(text=tweet)

print("Tweet posted successfully!", response)