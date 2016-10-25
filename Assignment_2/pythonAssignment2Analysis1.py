#!/usr/bin/python

import json
import argparse

parser = argparse.ArgumentParser(description='Search twitter api.')
# input_file=open("/Users/KurtWang/Desktop/study/twitterOutput.json", "r")
parser.add_argument("file", help="end date for tweet")
args = parser.parse_args()

result = []
input_file=open(args.file, "r")
json_decode=json.load(input_file)
for item in json_decode:
    value=item.get("favorite_count")
    
    if value == 0:
    	value = item.get("retweeted_status").get("favorite_count")
    print value
    result.append(value)
print("average likes of most recent 200 tweets: ")
print(sum(result) / float(len(result)))