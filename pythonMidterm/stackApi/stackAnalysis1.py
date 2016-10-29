#!/usr/bin/python

import json
import os
import sys
import argparse
# from stackauth import StackAuth
# from stackexchange import Site, StackOverflow
from stackpy import API, Site
from stackapi import StackAPI
from datetime import datetime

result = []
my_dictionary = {}

input_file = open("/Users/KurtWang/Desktop/study/stackApi/stackOutput.json", "r")
# input_file=open(args.file, "r")
json_decode=json.load(input_file)
for item in json_decode:
	title = item.get("title")
	userId = item.get("owner").get("user_id")

	print title
	print userId

	site = StackAPI('stackoverflow')
	user = site.fetch('users/{ids}', ids=userId)
	
	for u in user["items"]:
		badgeCount = u.get("badge_counts").get("bronze") + u.get("badge_counts").get("silver") + u.get("badge_counts").get("gold")

	print badgeCount
	my_dictionary[title] = badgeCount
	break

# count = 10
print("badge count by reverse order: ")
for w in sorted(my_dictionary, key=my_dictionary.get, reverse=True):
	# count -= 1

	# if count < 0:
	# 	break

	print w, my_dictionary[w]