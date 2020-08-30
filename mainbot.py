import tweepy
import time

print('Hi, I am INVERSO BOT')
#Authenticate to Twitter
CONSUMER_KEY = 'j9EBVirfj1Eqs5WTUqhwpzBcT'
CONSUMER_SECRET = 'h92D3IEZvqtiYciKmb7EpiQ25dNSX8wbjbUtBmG7gAXGZixheW'
ACCESS_KEY = '1379945563-UJ1IRwZrCiDx8yjyhAGm0Qyk6k9myfmnm4Rdaki'
ACCESS_SECRET = 'RqWeQXTlFS7nunq9KqYWuyTaDZqQO1XPDAXph3tIaToeP'

#Setting up connection
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user= api.me()
search = [ '#cybersecurity','#womenwhocode','#100DaysOfCode','#diazonic']
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

