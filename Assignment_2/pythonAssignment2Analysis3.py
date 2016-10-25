#!/usr/bin/python

import json
import argparse

parser = argparse.ArgumentParser(description='Search twitter api.')
parser.add_argument("file", help="end date for tweet")
args = parser.parse_args()

my_dictionary = {}
# input_file=open("/Users/KurtWang/Desktop/study/trump/twitterOutputTrump.json", "r")
input_file=open(args.file, "r")
json_decode=json.load(input_file)

for item in json_decode:
	key = item.get("text")
	my_dictionary[key] = item.get("retweet_count")
    
# print("tweets and retweet count: ")
# for w in my_dictionary:
# 	print w, my_dictionary[w]

count = 10
print("retweet count by reverse order: ")
for w in sorted(my_dictionary, key=my_dictionary.get, reverse=True):
	count -= 1

	if count < 0:
		break

	print w, my_dictionary[w]


