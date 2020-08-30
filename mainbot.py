from __future__ import unicode_literals
import tweepy
import time
import os

print('Hi, I am INVERSO BOT')
#Authenticate to Twitter

CONSUMER_KEY = os.getenv('consumer_key')
CONSUMER_SECRET = os.getenv('consumer_secret')
ACCESS_KEY = os.getenv('access_token')
ACCESS_SECRET = os.getenv('access_token_secret')

#Setting up connection
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user= api.me()
search = '#diazonic'
num_tweet = 350

#fetching tweets
for tweet in tweepy.Cursor(api.search, search).items(num_tweet):
	try:
		print('Tweet Liked')
		tweet.favorite()
		
		print('Retweet done')
		tweet.retweet()
		time.sleep(10)
		
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

         
