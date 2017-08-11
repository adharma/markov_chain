import json
import glob

from pprint import pprint

with open("tweets_trump_final.json", "r") as data_file:
	data = json.load(data_file)
print "reading JSON file+++++++++"

counter = 1
for i in range(0, len(data)):
	print str(counter) + " " + (data[i]["text"])
	counter += 1
	print "\n"

# print "total number of tweets collected: %d" % (counter)