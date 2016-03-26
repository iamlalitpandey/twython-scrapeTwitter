# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 00:24:10 2016

@author: lalit
"""
# CODE CONTAINS MULTIPLE TEST CASES - RUN IN BLOCKS ONLY (try-catch blocks)

# apicodes contains the API keys/secret keys /access_tokens compiled in below format -
#consumer_key="xxxxxxxxxxx"
#consumer_secret="xxxxx"
#access_token="xxxx"
#access_token_secret="xxxxxxxx"


from apicodes import *
from twython import Twython,TwythonError,TwythonStreamer

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

##### self tweeted data
try:
    user_timeline = twitter.get_user_timeline(screen_name='iamlalitpandey')
except TwythonError as e:
    print e

for tweets in user_timeline:
    print (tweets['text']+"\n")
#--------------------------------------
    
##### Home twits 20 
i=1
public_tweets = twitter.get_home_timeline()
for tweet in public_tweets:
    print (str(i)+"\n")
    print tweet['text']
    i+=1
#--------------------------------------
  
# Try catch block to update status 
try:
   twitter.update_status(status='Hey there, This is a test code')
except TwythonError as e:
    print e    
#--------------------------------------    

#Try catch block to search,specify query text as q='querytext'    

try:
    search_results = twitter.search(q='#AAPL', count=50)
except TwythonError as e:
    print e
  

for tweet in search_results['statuses']:
    print 'Tweet from @%s on Date: %s' % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at'])
    print tweet['text'].encode('utf-8'), '\n'
#--------------------------------------    
    
#### live twits section 
class liveStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
            #time.sleep(0.2)
        # Want to disconnect after the first result?
        # self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data

# Requires Authentication as of Twitter API v1.1
data = liveStreamer(consumer_key, consumer_secret, access_token, access_token_secret)

#filter status data with search keyword track='icc'
data.statuses.filter(track='icc')    

#--------------------------------------    
    
    
    
    
    
    
    
    
    
    
    
    