#!/usr/bin/python

import argparse
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# get month 
parser = argparse.ArgumentParser(description='search for month')
parser.add_argument("months", help="month")
parser.add_argument("dayOfWeek", help="day of week")
args = parser.parse_args()

# read the carrierOriginDest.csv file and get number of each origin and destination city
month = pd.read_csv('~/Downloads/flightData/flightday.csv', sep=",", usecols = ["Month", "DayOfWeek"])
# flightByMonthArray = month.Month.unique()
# dayofWeekArray = month.DayOfWeek.unique()
flights = len(month.index)

flightByMonthCountDict = {}
dayofWeekCountDict = {}

print "flight by month and count"

for i in range(1, 13):
    print i
    countByMonth = month.loc[month['Month'] == i]
    print len(countByMonth.index)
    flightByMonthCountDict[i] = len(countByMonth.index)
    # originCountArray.append(len(countByOrigin.index))

print "**************************************************"
print "flight by day of week and count"

for i in range(1, 8):
    print i
    countBydayofWeek = month.loc[month['DayOfWeek'] == i]
    print len(countBydayofWeek.index)
    dayofWeekCountDict[i] = len(countBydayofWeek.index)
    # originCountArray.append(len(countByOrigin.index))

monthArray = list(flightByMonthCountDict.keys())
countByMonthArray = list(flightByMonthCountDict.values())

x = monthArray
y = countByMonthArray
plt.xticks(monthArray)
# plt.yticks(countByMonthArray)
plt.plot(x, y)
plt.title('Total flights by month')
plt.ylabel('Number of flights')
plt.xlabel('Month')
plt.show()


dayOfWeekArray = list(dayofWeekCountDict.keys())
countByDayOfWeekArray = list(dayofWeekCountDict.values())

x = dayOfWeekArray
y = countByDayOfWeekArray
plt.plot(x, y)
plt.title('Total flights by day of week')
plt.ylabel('Number of flights')
plt.xlabel('Day of week')
plt.show()


monthDict = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
weekDict = {'1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Friday', '6': 'Saturday', '7': 'Sunday'}


# create pie chart by specific month
explode = (0.1, 0)
colors = ['blue', 'green']
m = monthDict.get(args.months)
labels = [m, 'Other month']
number = month.loc[month['Month'] == int(args.months)]
number = len(number)
rest = flights - number
sizes = [number, rest]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of flights by month')
plt.show()

# create pie chart by specific day of week
explode = (0.1, 0)
colors = ['blue', 'green']
day = weekDict.get(args.dayOfWeek)
labels = [day, 'Other dayOfWeek']
number = month.loc[month['DayOfWeek'] == int(args.dayOfWeek)]
number = len(number)
rest = flights - number
sizes = [number, rest]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of flights by day of week')
plt.show()


