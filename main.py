import tweepy
from keys import api_key, api_secret_key, access_token, access_token_secret
import requests
import json 
import time
from datetime import datetime, timedelta



def auth():
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def new_tweet():
    api = auth()
    for tweet in api.user_timeline(count=100,exclude_replies=True, include_rts=False) :
        try:
            created_at = tweet.created_at 
            difference = datetime.today() - created_at
            if timedelta(days=1) < difference <timedelta(days=2):
                    print(tweet.text)
                    tweet.retweet()
                    print("SUCCESSFUL")
        except tweepy.TweepError as error:
            print("ERROR: ", error)
new_tweet()
# while True:
    # time.sleep(60*60)
    