import re
import json
import glob
import time
from markov_python.cc_markov import MarkovChain
from pprint import pprint

tweet_length = 166
counter = 1
mc = MarkovChain()
run = True

"""read merged JSON file trump_tweets --- into data variable"""
print "reading trump tweets from JSON file"
time.sleep (5)
with open("trump_tweets.json", "r") as data_file:
	data = json.load(data_file)

"""add each tweet, line by line, to the Markov Chain instance mc"""
for i in range(0, len(data)):
	print (data[i]["text"])
	mc.add_string(data[i]["text"])
	counter += 1
print "\ntotal number of tweets collected: %d \n" % (counter)
time.sleep (5)

"""Generate Markov tweets, and match the first element with a specific word"""
print "generating Markov tweets"
print "*****\n"
time.sleep (5)
total_time = 0
t1 = time.time()
while run == True:
	full_tweet = u' '.join(mc.generate_text(tweet_length))
	first_word = full_tweet.split(' ', 1)[0]
	second_word = full_tweet.split(' ', 2)[1]
	third_word = full_tweet.split(' ', 3)[2]
	fourth_word = full_tweet.split(' ', 4)[3]
	if first_word == "i" and second_word == "am":
		print "Full tweet: "+ full_tweet
		t2 = time.time()
		total_time = t2-t1
		print "total time to find 'i am': " + str(total_time) + "s"
		run = False
	else:
		print "generated tweet does not match...trying again. " + first_word + " " + second_word + " " + third_word + " " + fourth_word
	
