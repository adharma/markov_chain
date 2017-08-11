import json
import glob
import time
from markov_python.cc_markov import MarkovChain
from pprint import pprint

print "reading trump tweets from JSON file"
time.sleep (2)
with open("trump_tweets.json", "r") as data_file:
	data = json.load(data_file)

counter = 1
mc = MarkovChain()
for i in range(0, len(data)):
	print (data[i]["text"])
	mc.add_string(data[i]["text"])
	counter += 1
print "total number of tweets collected: %d \n" % (counter)

tweet_length = 166
print "generating Markov tweets"
print "***** \n"
time.sleep (2)
for i in range(10):
	print "Markov Trump tweet-->" + u' '.join(mc.generate_text(tweet_length))
