#!/usr/bin/env python

from secret import *
import tweepy
import time
import random


auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

idFile=open("lastID.txt")
lastTweet=idFile.readline()

while True:
	
	mentionList = api.mentions_timeline(count=1)
	for mention in mentionList:
                
		if(lastTweet != str(mention.id)):
			lineList = open("quotes.txt").read().splitlines()
			quote = random.choice(lineList)
			tweet_body = "@" + mention.user.screen_name + " " + quote.decode('utf-8')
			while(len(tweet_body) > 140):
                                quote = random.choice(lineList)
                                tweet_body = "@" + mention.user.screen_name + " " + quote.decode('utf-8')        
                        api.update_status(tweet_body ,mention.id)
			lastTweet=str(mention.id)
                        idFile=open("lastID.txt",'w')
                        idFile.write(str(lastTweet))
                        
                        
			
	time.sleep(30)

idFile.close()
