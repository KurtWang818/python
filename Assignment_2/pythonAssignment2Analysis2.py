#!/usr/bin/python

import json
import argparse

parser = argparse.ArgumentParser(description='Search twitter api.')
parser.add_argument("file", help="end date for tweet")
args = parser.parse_args()

result1 = []
# input_file1=open("/Users/KurtWang/Desktop/study/trump/twitterOutputTrump.json", "r")
input_file=open(args.file, "r")
json_decode1=json.load(input_file1)
for item1 in json_decode1:
    value1=item1.get("user").get("friends_count")
    
    print value1
    result1.append(value1)
print("average friends count for user who tweets Trump: ")
print(sum(result1) / float(len(result1)))

result2 = []
input_file2=open("/Users/KurtWang/Desktop/study/hillary/twitterOutputHillary.json", "r")
json_decode2=json.load(input_file2)
for item2 in json_decode2:
    value2=item2.get("user").get("friends_count")
    
    print value2
    result2.append(value2)
print("average friends count for user who tweets Hillary: ")
print(sum(result2) / float(len(result2)))