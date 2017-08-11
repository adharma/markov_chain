import json
from pprint import pprint

with open("tweets_trump.json", "r") as data_file:
	data = json.load(data_file)
print "******************"

for i in range(0, len(data)):
	print (data[i]["text"])
	print "\n"