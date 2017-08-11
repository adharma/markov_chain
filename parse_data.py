import os
import re
import json
import glob
import time
from markov_python.cc_markov import MarkovChain
from pprint import pprint


"""initative variables and instances"""
tweet_length = 10
counter = 1
mc = MarkovChain()
run = True
sleep_time = 5

"""clear screen"""
os.system('clear')

"""read merged JSON file trump_tweets --- into data variable"""
print "\n****************************************"
print "reading trump tweets from JSON file"
print "****************************************\n"
time.sleep (sleep_time)
with open("trump_tweets.json", "r") as data_file:
	data = json.load(data_file)

"""add the text of each tweet, line by line, to the Markov Chain instance 'mc'"""
for i in range(0, len(data)):
	print (data[i]["text"])
	mc.add_string(data[i]["text"])
	counter += 1
time.sleep (sleep_time)

"""clear screen"""
os.system('clear')
print "\n****************************************"
print "tweets collected: %d" % (counter)
print "****************************************\n"
time.sleep (sleep_time)

"""get start of tweet as inputs from user"""
print "To help us generate an appropriate Trump tweet for you - enter 2 words."
user_first_word = raw_input("Enter the first word:\n")
user_second_word = raw_input("Enter the second word:\n")
# user_third_word = raw_input("Enter the third word of your tweet:\n")

"""clear screen"""
os.system('clear')

"""Generate Markov tweets, and matches leading words of the string, with the user inputs"""
print "\n****************************************"
print "generating Markov tweets"
print "****************************************\n"
time.sleep (sleep_time)
total_time = 0
t1 = time.time()
while run == True:
	full_tweet = u' '.join(mc.generate_text())
	print full_tweet
	first_word = full_tweet.split(' ', 1)[0]
	second_word = full_tweet.split(' ', 100)[1]
	# third_word = full_tweet.split(' ', 100)[2]
	phrase = user_first_word + " " + user_second_word
	if re.search(phrase, full_tweet): #str(phrase) in full_tweet:
		os.system('clear')
		print "\n*----->matched tweet: %s\n" % full_tweet
		t2 = time.time()
		total_time = t2-t1
		print "\n*----->total time to find '%s %s': %ds\n" % (user_first_word, user_second_word, total_time)
		run = False
	else:
		pass
		#print "generated tweet does not match...trying again. " + first_word + " " + second_word + " " + third_word + " " + fourth_word
	
