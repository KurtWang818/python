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

score_map = {}

for item in json_decode:
	title = item.get("title")
	score = item.get("score")

	score_map[title] = score

print("score by reverse order: ")
for w in sorted(score_map, key=score_map.get, reverse=True):
	
	print w, score_map[w]







