#!/usr/bin/python

import argparse
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# get the airport of the city
parser = argparse.ArgumentParser(description='search for city')
parser.add_argument("city", help="city")
args = parser.parse_args()

# read the carrierOriginDest.csv file and get number of each origin and destination city
city = pd.read_csv('~/Downloads/flightData/carrierOriginDest.csv', sep=",", usecols = ["Origin", "Dest"])
originArray = city.Origin.unique()
destArray = city.Dest.unique()
flights = len(city.index)

originCountDict = {}
destCountDict = {}

print "origin city and count"

for i in originArray:
    # print i
    countByOrigin = city.loc[city['Origin'] == i]
    # print len(countByOrigin.index)
    originCountDict[i] = len(countByOrigin.index)
    # originCountArray.append(len(countByOrigin.index))

print "**************************************************"
print "destination city and count"

for i in destArray:
    # print i
    countByDest = city.loc[city['Dest'] == i]
    # print len(countByDest.index)
    destCountDict[i] = len(countByDest.index)
    # destCountArray.append(len(countByDest.index))

count1 = 10
toporiginCountDict = {}
count2 = 10
topdestCountDict = {}

print "**************************************************"
print "top origin city and count"

for c in sorted(originCountDict, key=originCountDict.get, reverse = True):
	count1 -= 1

	if count1 < 0:
		break

	toporiginCountDict[c] = originCountDict[c]
	# print c, originCountDict[c]
		
print "**************************************************"
print "top destination city and count"

for c in sorted(destCountDict, key=destCountDict.get, reverse = True):
	count2 -= 1

	if count2 < 0:
		break

	topdestCountDict[c] = destCountDict[c]
	# print c, destCountDict[c]

# combine origin city and destination city
print "**************************************************"
print "count for routes"
def f(x):
	return x['Origin'] + "->" + x['Dest']

city["Route"] = city.apply(f, axis = 1)
routeArray = city.Route.unique()
routeCountDict = {}

for i in routeArray:
    print i
    countByRoute = city.loc[city['Route'] == i]
    print len(countByRoute.index)
    routeCountDict[i] = len(countByRoute.index)
    # originCountArray.append(len(countByOrigin.index))

count3 = 10
topRouteCountDict = {}

print "**************************************************"
print "top route and count"

for c in sorted(routeCountDict, key=routeCountDict.get, reverse = True):
	count3 -= 1

	if count3 < 0:
		break

	topRouteCountDict[c] = routeCountDict[c]
	print c, routeCountDict[c]

# create bar chart for number of flights by route

topRouteArray = list(topRouteCountDict.keys())
topRouteCountArray = list(topRouteCountDict.values())

y_pos = np.arange(len(topRouteCountDict))
plt.bar(y_pos, topRouteCountArray, align='edge', alpha=0.5)
plt.xticks(y_pos, topRouteArray)
plt.ylabel('Number of flights')
plt.title('Total numbe of flights by route')
 
plt.show()

# create bar chart for number of flights by origin

toporiginArray = list(toporiginCountDict.keys())
toporiginCountArray = list(toporiginCountDict.values())

y_pos = np.arange(len(toporiginCountDict))
plt.bar(y_pos, toporiginCountArray, align='edge', alpha=0.5)
plt.xticks(y_pos, toporiginArray)
plt.ylabel('Number of flights')
plt.title('Total numbe of flights by origin city')
 
plt.show()

# create bar chart for number of flights by destination

topdestArray = list(topdestCountDict.keys())
topdestCountArray = list(topdestCountDict.values())

y_pos = np.arange(len(toporiginCountDict))
plt.bar(y_pos, topdestCountArray, align='edge', alpha=0.5)
plt.xticks(y_pos, topdestArray)
plt.ylabel('Number of flights')
plt.title('Total numbe of flights by destination city')
 
plt.show()

# create pie chart by specific origin city
explode = (0.1, 0)
colors = ['blue', 'green']
labels = [args.city, 'Other city']
number = city.loc[city['Origin'] == args.city]
number = len(number)
rest = flights - number
sizes = [number, rest]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of flights by origin city')
plt.show()

# create pie chart by specific destination city
explode = (0.1, 0)
colors = ['blue', 'green']
labels = [args.city, 'Other city']
number = city.loc[city['Dest'] == args.city]
number = len(number)
rest = flights - number
sizes = [number, rest]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of flights by destination city')
plt.show()



