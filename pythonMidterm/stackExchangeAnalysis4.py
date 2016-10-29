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

reputation_map = {}

for item in json_decode:
	reputation = item.get("reputation")
	display_name = item.get("display_name")

	reputation_map[display_name] = reputation

print("reputation by reverse order: ")
for w in sorted(reputation_map, key=reputation_map.get, reverse=True):
	
	print w, reputation_map[w]





