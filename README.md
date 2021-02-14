# Reach-Retweet
[![built with Love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/jai-dewani/)

This bot has one job: To retweet your yesterday's tweet so they can live a little longer on your followers timeline. 

# Here is how you can try this yourself 

## Close this repo 
```
git clone https://github.com/jai-dewani/Reach-Retweet.git
```
## Install [Tweepy](http://www.tweepy.org/)
```
pip install tweepy
```
## Get your twitter developer keys
Make sure to get all four api_key, api_secret_key, access_token and access_token_secret, you might have to do some extra steps for the last two. Refer [twitter's getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/guide) for detailed steps 

## Save the keys your genrated 
Make sure to save the keys in the `keys.py` file, I have provided a sample how they should be stored. 

## Let's learn how to use the application
```
python main.py
```
When run once it will look for all your tweeets from yesterday and retweet them as you only (you gave the script your identity by providing those magical credentials).

If you want you can create a service and run this script once everyday so your tweets get the most impressions from your followers and their followers :) 

 > Do give this repo a star, if you loved this small project I made in my weekends!