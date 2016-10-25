#!/usr/bin/python

import json
import oauth2 as oauth
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import argparse
import os
import time
from datetime import date

# consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
# access_token = oauth.Token(key=access_token, secret=access_token_secret)
# client = oauth.Client(consumer, access_token)

# search = "https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi"

# response, data = client.request(search)

parser = argparse.ArgumentParser(description='Search twitter api.')
parser.add_argument("echo", help="twitter topic")
parser.add_argument("since", help="start date for tweet")
parser.add_argument("until", help="end date for tweet")
parser.add_argument("directory", help="end date for tweet")
args = parser.parse_args()

def createFolder():
    
	# if not os.path.exists("/Users/KurtWang/Desktop/study"):
	# 	os.makedirs("/Users/KurtWang/Desktop/study")
	# else:
	# 	print ("/Users/KurtWang/Desktop/study exists already")

	if not os.path.exists(args.directory):
		os.makedirs(args.directory)
	else:
		print (args.directory + " exists already")


def query(): 
	consumer_key = "BxVO33D4Hm6SEGiehkfuhfvjC"
	consumer_secret = "jGkNo6gAE25V17SeViXhj87xxCcvqJrlbp5soWhy5fbCSIJty8"
	access_token = "788617823329382400-HjpvjKgyBx2QFqjNyBswZuBqIqbprxC"
	access_token_secret	= "90bmuuYc4l7heomNbn1JqI8F7bEIDrISSvNBSKkwYDpet"

	oauth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret)
	twitter = Twitter(auth=oauth)
	twitter_stream = TwitterStream(auth=oauth)
	
	# mrvincecarter15

	# iterator = twitter_stream.statuses.filter(track=args.echo, language="en", since="2014-9-1", until="2014-9-5")
	# iterator = twitter.statuses.user_timeline(screen_name=args.echo, count=1000, since="2015-10-15", until="2015-10-17")
	iterator = twitter.search.tweets(q=args.echo, count=100, since=args.since, until=args.until)
	tweet_count = 100

	if not os.path.exists(args.directory + "/" + args.echo):
		os.makedirs(args.directory + "/" + args.echo)
	else:
		print (args.directory + "/" + args.echo + " exists already")

	f = open(args.directory + "/" + args.echo + "/twitterOutputWithDate.json", 'w+')
	f.write("[")
	for tweet in iterator["statuses"]:
	# for tweet in iterator:
	    tweet_count -= 1

	    if tweet_count < 0:
	    	break

	    if tweet_count == 0:
	    	f.write(json.dumps(tweet))
	    	continue

	    f.write(json.dumps(tweet))
	    f.write(",") 
	    f.write("\n")
	    
	f.write("]")

createFolder()
query()
   




