#!/usr/bin/env python3
#
# TwitterBot3000
# by,
# Mike Tieden (@miketieden)
#
import tweepy
import config
import random
import time
from datetime import datetime

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.ckey, config.csecret)
auth.set_access_token(config.atoken, config.asecret)

# Create API object
api = tweepy.API(auth)

# Timestamp Format
f = "%d.%^b.%Y %H:%M:%S"

# Start Script
def rt(api, screen_name):
    try:
        api.retweet(screen_name)
        t = datetime.now()
        timestamp = t.strftime(f)
        print(timestamp + " Retweeting: " + str(screen_name))
    except:
        pass
print()
print()
print(" +--------------------+")
print(" |                    |")
print(" |   TwitterBot3000   |")
print(" |                    |")
print(" +--------------------+")
time.sleep(3)
print()
print()
t = datetime.now()
timestamp = t.strftime(f)
print(timestamp + " Scanning...")
while True:
    for username in config.usernames:
        tweets = api.user_timeline(screen_name=username, count=1)
        for tweet in tweets:
                rt(api, tweet.id)
    t = datetime.now()
    timestamp = t.strftime(f)
    print(timestamp + " Pausing for " + str(config.m) + " minutes.")
    time.sleep(config.m*60)
    print()
    print("New Scan")
    t = datetime.now()
    timestamp = t.strftime(f)
    print(timestamp + " Scanning...")
