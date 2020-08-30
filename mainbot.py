import tweepy
import time

print('HII, I am INVERSO BOT')
#Authenticate to Twitter
CONSUMER_KEY = 'rDT7cwwQLTaIzeGJJ5EwE9eNu'
CONSUMER_SECRET = 'VXhRk6HKXr9nXrfWCTVdZBugOobD5KwZwZjZYSXghaG9o9AJ0w'
ACCESS_KEY = '1299783980783288320-9sj0K3TrsJYDs94dsGl3546mOC1Tme'
ACCESS_SECRET = 'k4afSrHPElDjqhP3ucvZo5UXTLPDMT0auXqCJScHAIap1'

#Setting up connection
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
api.verify_credentials()
print('API Created')

user= api.me()
search = '#womenwhocode'
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

