#!/usr/bin/python

import json
import os
import sys
import argparse
import requests

parser = argparse.ArgumentParser(description='Search stack exchange api.')
parser.add_argument("directory")
args = parser.parse_args()

input_file = open(args.directory + "/stackApi/stackUserOutput.json", "r")
# input_file=open(args.file, "r")
json_decode=json.load(input_file)

gold = {}
silver = {}
bronze = {}

for item in json_decode:
	displayName = item.get("display_name")
	gold_count = item.get("badge_counts").get("gold")
	silver_count = item.get("badge_counts").get("silver")
	bronze_count = item.get("badge_counts").get("bronze")

	if gold_count > 0:
		gold[displayName] = gold_count

	if silver_count > 0:
		silver[displayName] = silver_count

	if bronze_count > 0:
		bronze[displayName] = bronze_count

print("gold badge count by reverse order: ")
for w in sorted(gold, key=gold.get, reverse=True):
	
	print w, gold[w]

print("silver badge count by reverse order: ")
for w in sorted(silver, key=silver.get, reverse=True):
	
	print w, silver[w]

print("bronze badge count by reverse order: ")
for w in sorted(bronze, key=bronze.get, reverse=True):
	
	print w, bronze[w]

print("number of people with gold badge: " + str(len(gold)))
print("number of people with silver badge: " + str(len(silver)))
print("number of people with bronze badge: " + str(len(bronze)))






