from markov_python.cc_markov import MarkovChain

import requests 
import time
from bs4 import BeautifulSoup
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
 
consumer_key = 'xgHTlWF80pl97gBZqBNzOkMB1'
consumer_secret = 'hYiBcF15yoXGgwV99uWsefx7fTkwGwUlSj6xaIt9q88cEvzQzp'
access_token = '245997170-UHKnopkqwGC42xWYEm4xf2XHIpMNsfNe5dFDXjkD'
access_secret = 'z48kgXn58JsCKKKh5djBQD6voAIlCKFEddrHiuQd64dip'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

user = api.get_user('asankadharma')
print "wow Asanka has: " + str(user.followers_count) + " followers!"
for friend in user.friends():
	print friend.screen_name

# class MyListener(StreamListener):
# 	def on_data(self, data):
# 		try:
# 			with open('trump2.json', 'a') as f:
# 				f.write(data)
# 				return True
# 		except BaseException as e:
# 			print("Error on_data: %s" % str(e))
#         	return True
#     	def on_error(self, status):
# 	        print(status)
# 	    	return True spot
# twitter_stream = Stream(auth, MyListener())
# twitter_stream.filter(track=['trump'])

# print twitter_stream
# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     print(status.text)

# """pull superpac info into page object"""
# page = requests.get("https://www.opensecrets.org/pacs/superpacs.php")
# print ("contents of page object... fresh from the interwebs")
# time.sleep(10)
# print (page.content)

# """parse the contents using BeautifulSoup, store in soup instance, parse using html)"""
# soup = BeautifulSoup(page.content, 'html.parser')


# print ("**************")
# print ("soup.prettify")
# time.sleep(10)
# print (soup.prettify())
# print ("soup children")
# time.sleep(10)
# list(soup.children)
# print ([type(item) for item in list(soup.children)])
# html = list(soup.children)[3]
# list(html.children)
# body = list(html.children)[4]
# list(body.children)
# p = list(body.children)[1]

# print "starting Markov Chain"
# time.sleep(1)
# mc = MarkovChain()
# mc.add_file(p)


# print "generating text"
# time.sleep(1)
# print mc.generate(text)

"""
example GUIDO input file
[ \clef<"treble"> \key<"D"> \meter<"4/4">
 a1*1/2 b a/4. g/8 f#/4 g a/2 b a/4. g/8 f#/4 g
 a/2 a b c#2/4 d c#/2 b1 a/1 ]
Use twitter APU to generate new musical notation from favouriite tracks using markor generator running
"""
