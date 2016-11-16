#!/usr/bin/env python

from secret import *
import tweepy
import time
import random


auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

lastUser=""

while True:
	
	mentionList = api.mentions_timeline(1)
	for mention in mentionList:
		if(lastUser != mention.user.screen_name):
			lineList = open("quotes.txt").read().splitlines()
			quote = random.choice(lineList)
			tweet_body = "@" + mention.user.screen_name + " " + quote.decode('utf-8')
			#print tweet_body
			api.update_status(tweet_body ,mention.id)
			lastUser=mention.user.screen_name
			
	time.sleep(30)
