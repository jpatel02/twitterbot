import tweepy
import json
import random

# Define our bot's constant variables
BOT_CONSUMER_KEY = '9ezltcrs4EQ2zRew8AExQWCIU'
BOT_CONSUMER_SECRET = 'lKo0ZMvP3tfsdFE2Rj4wXlZmolXwjg9Dv2yLTUFDU2lVKfsAhm'
BOT_ACCESS_KEY = '1959370119965986816-R0x7LeYrxQ7zXrVJd26XS6p2ZkSDZu'
BOT_ACCESS_SECRET = 'co0iavLCQKrgYeguiNl8x1jQm3nWJbtKiu1q9nCHXhr1F'
BOT_BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMT03gEAAAAANJGZr9QZYz90tmTTlpdvjAXxJhQ%3DbMMzAkOrBzCvxJIOaHSVlFg3k8tPXtw0L25zwrFPgRlrPwmJqx'

# Define the personal account's constant variables by reading the API keys from the encrypted text file
api_file = open("blocklist_api_keys.txt", "r")
file = api_file.readlines()
api_file.close()

ACCESS_KEY = file[0][14:64]
ACCESS_SECRET = file[1][21:66]
BEARER_TOKEN = file[2][14:126]
CONSUMER_KEY = file[3][9:34]
CONSUMER_SECRET = file[4][16:66]

# Authenticate to Twitter using OAuth 2.0 Bearer Token
client_bot = tweepy.Client(bearer_token=BOT_BEARER_TOKEN,
                       consumer_key=BOT_CONSUMER_KEY,
                       consumer_secret=BOT_CONSUMER_SECRET,
                       access_token=BOT_ACCESS_KEY,
                       access_token_secret=BOT_ACCESS_SECRET)

client_user = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET)

# Retrieving the personal account blocklist and initializing the list to store the users
blocked_list = client_user.get_blocked()
blocked_users = []
for x in range(len(blocked_list.data)):
    blocked_users.append(str(blocked_list.data[x]))

# Selecting the user to tweet about at random
target_user = random.choice(blocked_users)

# Storing the accessed users in a JSON file so repeat tweets are not possible
with open("tweeted_users.json", 'r+') as file:
    file_data = json.load(file)

    while target_user in file_data["tweeted_users"]:
        target_user = random.choice(blocked_users)
    
    file_data["tweeted_users"].append(target_user)

    file.seek(0)

    json.dump(file_data, file, indent=4)

# Posting the tweet
tweet = "The toxic user of the day is @" + target_user + "."
response2 = client_bot.create_tweet(text=tweet)

print("Tweet posted successfully!", response2)