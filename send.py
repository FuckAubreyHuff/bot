import tweepy
import time
import random

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

# File name for followers
file_name = 'followers.txt'

with open(file_name) as fn:
    follower_list = fn.readlines()
# Storing in a list
follower_list = [x.strip() for x in follower_list]

def get_insults(file_name):
    f = open(file_name, 'r')
    insults = f.read().split('\n')
    return insults

def pick_insult():
    insults = get_insults('insults.txt')
    insult = random.choice(insults)
    return insult

def reply():
    insult = pick_insult()
    for line in follower_list:
        api.update_status('@' + line + ' ' + insult)
        print('Sending a tweet - ' + '@' + line + ' ' + insult)
        time.sleep(15)

reply()
print("Tweeted those twits")
