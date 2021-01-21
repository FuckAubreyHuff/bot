import tweepy
import time

print("Bot Starting...")

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Define screen name (Twitter @) to use
screen_name = 'aubrey_huff'

# Number of followers to scrape
f_count = 10

# Function to save followers in a text file
def getting_followers(file):
    cursor = tweepy.Cursor(api.followers, screen_name)
    for user in cursor.items(f_count):
        file.write(str(user.screen_name)+ "\n")
        # Check if it's gathering data correctly
        #print("follower:" + user.screen_name)

with open("followers.txt", "w") as file:
    getting_followers(file)

print("Collected ids")
