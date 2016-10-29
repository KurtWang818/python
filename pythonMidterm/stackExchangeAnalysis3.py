#!/usr/bin/python

import json
import os
import sys
import argparse
import requests

parser = argparse.ArgumentParser(description='Search stack exchange api.')
parser.add_argument("directory")
args = parser.parse_args()

input_file = open(args.directory + "/stackApi/stackOutput.json", "r")
# input_file=open(args.file, "r")
json_decode=json.load(input_file)

answers = {}
tags_map = {}
tag_answer_map = {}

for item in json_decode:
	tags = item.get("tags")
	answersCount = item.get("answer_count")
	title = item.get("title")

	answers[title] = answersCount

	for tag in tags:
		if tag in tags_map:
			tags_map[tag] += 1
		else:
			tags_map[tag] = 1

	for tag in tags:
		if tag in tag_answer_map:
			tag_answer_map[tag] += answersCount
		else:
			tag_answer_map[tag] = answersCount


print("answers count by reverse order: ")
for w in sorted(answers, key=answers.get, reverse=True):
	
	print w, answers[w]

print("questions asked per tag by reverse order: ")
for w in sorted(tags_map, key=tags_map.get, reverse=True):
	
	print w, tags_map[w]

print("answers per tag by reverse order: ")
for w in sorted(tag_answer_map, key=tag_answer_map.get, reverse=True):
	
	print w, tag_answer_map[w]












