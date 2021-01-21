import tweepy
import time
import random

print("Bot Starting...")

CONSUMER_KEY = 'bfcVqgGo80zIXyR1Kbcg0ggAi'
CONSUMER_SECRET = 'P48ZPHiWMhaKXAkxAR8S9jiztAF6qAa3QynrA9PdTTmEgrxn4H'
ACCESS_TOKEN = '1176869078738378753-wY1noHWcRp4MGRDFuMSEvFFJxLXTId'
ACCESS_SECRET = 'EpiPeDFrRB2XzG4jgGt6tWp4p05ww4XwFUdXEQco4FPcS'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Define screen name (Twitter @) to use
screen_name = '69Data69'

# Function to save followers in a text file
def getting_followers(file):
    cursor = tweepy.Cursor(api.followers, screen_name)
    for user in cursor.items(500):
        file.write(str(user.screen_name)+ "\n")
        # Check if it's gathering data correctly
        #print("follower:" + user.screen_name)

with open("followers.txt", "w") as file:
    getting_followers(file)

print("Collected ids")
