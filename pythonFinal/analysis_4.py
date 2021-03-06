#!/usr/bin/python

from __future__ import division
import argparse
import pandas as pd
from pandas import *
from matplotlib import pyplot as plt
import numpy as np
import sys 
import os
import csv

path = os.path.split(os.path.realpath(sys.argv[0]))[0]


# get month 
parser = argparse.ArgumentParser(description='search for month')
parser.add_argument("months", help="month")
parser.add_argument("carrier", help="carrier")
args = parser.parse_args()

# read flightdelaybymonth.csv file and get Month UniqueCarrier ArrDelay and DepDelay values
files = [path + "/flightData/flightdelaybymonth_0.csv", path + "/flightData/flightdelaybymonth_1428385.csv", path + "/flightData/flightdelaybymonth_2856770.csv", path + "/flightData/flightdelaybymonth_4285155.csv", path + "/flightData/flightdelaybymonth_5713540.csv"]
# month = pd.read_csv(path + '/flightData/flightdelaybymonth.csv', sep=",", usecols = ["Month", "UniqueCarrier", "ArrDelay", "DepDelay"])
month = concat([read_csv(f, sep=",", usecols = ["Month", "UniqueCarrier", "ArrDelay", "DepDelay"]) for f in files], keys=files)
carrierArray = month.UniqueCarrier.unique()
flights = len(month.index)

flightByMonthCountDict = {}
print "flight by month and count"

for i in range(1, 13):
    print i
    countByMonth = month.loc[month['Month'] == i]
    print len(countByMonth.index)
    flightByMonthCountDict[i] = len(countByMonth.index)
    # originCountArray.append(len(countByOrigin.index))


departdelayflightByMonthCountDict = {}
print "delay flights by month and count"

for i in range(1, 13):
    print i
    countByMonth = month.loc[month['Month'] == i]
    # countByMonth['DepDelay'].replace('', np.nan, inplace = True)
    # countByMonth.dropna(subset = ['DepDelay'], inplace = True)
    countByMonth = countByMonth.loc[month['DepDelay'] > 0.0]
    print len(countByMonth.index)
    departdelayflightByMonthCountDict[i] = len(countByMonth.index)
    # originCountArray.append(len(countByOrigin.index))

departdelayflightByMonthPercentageDict = {}
for i in range(1, 13):
	print i
	percent = int(departdelayflightByMonthCountDict.get(i)) / int(flightByMonthCountDict.get(i))
	print percent
	departdelayflightByMonthPercentageDict[i] = percent

monthArray = list(departdelayflightByMonthPercentageDict.keys())
departpercentArray = list(departdelayflightByMonthPercentageDict.values())
# create bar chart for percentage of delayed flight by month

y_pos = np.arange(12)

plt.bar(y_pos, departpercentArray, align='edge', alpha=0.5)
plt.xticks(y_pos, monthArray)
plt.ylabel('percentage')
plt.title('Percentage of departure delay flights by month')
 
plt.savefig(path + '/pythonFinalscreen/image12.png')
plt.show()

arrivedelayflightByMonthCountDict = {}
print "delay flights by month and count"

for i in range(1, 13):
    print i
    countByMonth = month.loc[month['Month'] == i]
    # countByMonth['DepDelay'].replace('', np.nan, inplace = True)
    # countByMonth.dropna(subset = ['DepDelay'], inplace = True)
    countByMonth = countByMonth.loc[month['ArrDelay'] > 0.0]
    print len(countByMonth.index)
    arrivedelayflightByMonthCountDict[i] = len(countByMonth.index)
    # originCountArray.append(len(countByOrigin.index))

arrivedelayflightByMonthPercentageDict = {}

for i in range(1, 13):
	print i
	percent = int(arrivedelayflightByMonthCountDict.get(i)) / int(flightByMonthCountDict.get(i))
	print percent
	arrivedelayflightByMonthPercentageDict[i] = percent

monthArray = list(arrivedelayflightByMonthPercentageDict.keys())
arrivepercentArray = list(arrivedelayflightByMonthPercentageDict.values())
# create bar chart for percentage of delayed flight by month

y_pos = np.arange(12)

plt.bar(y_pos, arrivepercentArray, align='edge', alpha=0.5)
plt.xticks(y_pos, monthArray)
plt.ylabel('percentage')
plt.title('Percentage of arrival delay flights by month')
 
plt.savefig(path + '/pythonFinalscreen/image13.png')
plt.show()

totaldepartdelay = 0
totalarrivedelay = 0
for i in range(1, 13):
	number1 = departdelayflightByMonthCountDict.get(i)
	number2 = arrivedelayflightByMonthCountDict.get(i)
	totaldepartdelay += number1
	totalarrivedelay += number2
print totaldepartdelay
print totalarrivedelay

monthDict = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
weekDict = {'1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Friday', '6': 'Saturday', '7': 'Sunday'}
monthArray = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
weekArray = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# create pie chart for percentage of depart delay flight by month
explode = (0.1, 0)
colors = ['blue', 'green']
day = monthDict.get(args.months)
labels = [day, 'other month']
number = departdelayflightByMonthCountDict.get(i)
rest = totaldepartdelay - number
sizes = [number, rest]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of depart delay by month')

plt.savefig(path + '/pythonFinalscreen/image14.png')
plt.show()

# create pie chart for percentage of arrive delay flight by month
explode = (0.1, 0)
colors = ['blue', 'green']
day = monthDict.get(args.months)
labels = [day, 'other month']
number = arrivedelayflightByMonthCountDict.get(i)
rest = totalarrivedelay - number
sizes = [number, rest]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of arrive delay by month')

plt.savefig(path + '/pythonFinalscreen/image15.png')
plt.show()



carrierCountArray = {}
for i in carrierArray:
    print i
    countByCarrier = month.loc[month['UniqueCarrier'] == i]
    print len(countByCarrier.index)
    carrierCountArray[i] = (len(countByCarrier.index))


carrierdelayCountArray = {}
for i in carrierArray:
    print i
    countByCarrier = month.loc[month['UniqueCarrier'] == i]
    countByCarrier = countByCarrier.loc[month['ArrDelay'] > 0.0]
    print len(countByCarrier.index)
    carrierdelayCountArray[i] = (len(countByCarrier.index))

arrivedelayflightByCarrierPercentageDict = {}

for i in carrierArray:
	print i
	percent = int(carrierdelayCountArray.get(i)) / int(carrierCountArray.get(i))
	print percent
	arrivedelayflightByCarrierPercentageDict[i] = percent

carrierArray = list(arrivedelayflightByCarrierPercentageDict.keys())
carrierpercentArray = list(arrivedelayflightByCarrierPercentageDict.values())
# create bar chart for percentage of delayed flight by month

y_pos = np.arange(len(carrierArray))

plt.bar(y_pos, carrierpercentArray, align='edge', alpha=0.5)
plt.xticks(y_pos, carrierArray)
plt.ylabel('percentage')
plt.title('Percentage of arrival delay flights by carrier')
 
plt.savefig(path + '/pythonFinalscreen/image16.png')
plt.show()

# create pie chart by specific carrier
explode = (0.1, 0)
colors = ['blue', 'green']
labels = [args.carrier, 'Other Carrier']
number = carrierdelayCountArray.get(args.carrier)
rest = totalarrivedelay - number
sizes = [number, rest]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of flights by carrier')

plt.savefig(path + '/pythonFinalscreen/image17.png')
plt.show()

csvfile = open(path + "/results/analysis4.csv", "w")
writer = csv.writer(csvfile)
title = ["Month", "Count"]
writer.writerow(title)
text1 = ["Departure delay", ""]
writer.writerow(text1)
for i in range(12):
    month = monthArray[i]
    count = departpercentArray[i]
    data = [month, count]
    writer.writerow(data)

text2 = ["Arrival delay", ""]
writer.writerow(text2)
for i in range(12):
    month = monthArray[i]
    count = arrivepercentArray[i]
    data = [month, count]
    writer.writerow(data)

text3 = ["Carrier", "Count"]
for i in range(len(carrierArray)):
    carrier = carrierArray[i]
    count = carrierpercentArray[i]
    data = [carrier, count]
    writer.writerow(data)



