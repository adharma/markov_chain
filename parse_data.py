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
sleep_time = 0

"""clear screen"""
os.system('clear')

"""read merged JSON file trump_tweets --- into data variable"""
print "\n****************************************"
print "reading trump tweets from JSON file into Markov generator"
print "****************************************\n"
time.sleep (sleep_time)
with open("trump_tweets.json", "r") as data_file:
	data = json.load(data_file)
# with open("/etc/apt/sources.list", "r") as sources:
#     lines = sources.readlines()
# with open("/etc/apt/sources.list", "w") as sources:
#     for line in lines:
#         sources.write(re.sub(r'^# deb', 'deb', line))

"""clean text of each tweet, then add each cleaned text line, to the Markov Chain instance 'mc'"""
for i in range(0, len(data)):
	print "cleaning tweet--> " + (data[i]["text"])
	string_clean1 = re.sub(r'@', '', data[i]["text"])
	string_clean2 = re.sub(r'#', '', string_clean1)
	string_clean3 = re.sub(r'http\S+', '', string_clean2)
	string_clean4 = re.sub(r'pic.twitter.com\S+', '', string_clean3)
	input_string = re.sub("(?m)^\s+", "", string_clean4)
	print "cleaned tweet--> " + input_string
	mc.add_string(input_string)
	counter += 1
time.sleep (sleep_time)

"""clear screen"""
os.system('clear')
print "\n****************************************"
print "tweets collected: %d" % (counter)
print "****************************************\n"
time.sleep (sleep_time)

"""get start of tweet as inputs from user"""
print "To help generate an appropriate Trump tweet for you - enter a 3 word phrase."
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
user_first_word = raw_input("Enter the first word:")
user_second_word = raw_input("Enter the second word:")
user_third_word = raw_input("Enter the third word:")

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
	"""generate and split generated text into words"""
	full_tweet = u' '.join(mc.generate_text())
	# print "full split array debug:" ### debugging
	# print full_tweet.split(' ') ### debugging
	""" check if full_tweet has 3 words"""
	while len(full_tweet.split(' ')) < 3 :
		full_tweet = u' '.join(mc.generate_text())
	else:
		pass
	"""replace @ mention symbols with blanks"""
	# for character in full_tweet:
	# 	return character.replace("@", ""),
	"""break full_tweet into first 3 words"""
	first_word = full_tweet.split(' ', 1)[0]
	second_word = full_tweet.split(' ', 2)[1]
	third_word = full_tweet.split(' ', 3)[2]
	# print "\nDEBUG===> first + second + third: " + first_word + " " + second_word + " " + third_word ### debugging
	# print "\nDEBUG===> full: " + full_tweet ### debugging
	"""concatenate user inputs into a phrase"""
	phrase = user_first_word + " " + user_second_word + " " + user_third_word
	if re.search(phrase, full_tweet):
		os.system('clear')
		print "*----->matched tweet: %s\n" % full_tweet
		t2 = time.time()
		total_time = t2-t1
		print "*----->total time to find '%s %s %s': %ds\n" % (user_first_word, user_second_word, user_third_word, total_time)
		run = False
	else:
		print "generated text does not match...trying again. " + first_word + " " + second_word + " " + third_word
