import json
import glob
import time
from markov_python.cc_markov import MarkovChain
from pprint import pprint


with open("trump_tweets.json", "r") as data_file:
	data = json.load(data_file)
print "reading JSON file+++++++++"

counter = 1
mc = MarkovChain()
for i in range(0, len(data)):
	print (data[i]["text"])
	mc.add_string(data[i]["text"])
	counter += 1
	print "***** \n"

print "total number of tweets collected: %d \n" % (counter)

# mc.add_file("trump_tweets.json")

tweet_length = 5
print "generating Markov tweets"
print "***** \n"
time.sleep (2)
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
print "generating potential tweet from Trump-->" + u' '.join(mc.generate_text(tweet_length))
