#!/usr/bin/python

import argparse
import pandas as pd
from pandas import *
from matplotlib import pyplot as plt
import numpy as np
import sys 
import os

path = os.path.split(os.path.realpath(sys.argv[0]))[0]


# get carrier
parser = argparse.ArgumentParser(description='search for carrier')
parser.add_argument("carrier", help="carrier")
args = parser.parse_args()

files = [path + "/flightData/carrierOriginDest_0.csv", path + "/flightData/carrierOriginDest_1785550.csv", path + "/flightData/carrierOriginDest_3571100.csv", path + "/flightData/carrierOriginDest_5356650.csv"]
# origin = pd.read_csv(path + '/flightData/carrierOriginDest.csv', sep=",", usecols = ["UniqueCarrier", "Origin"])
origin = concat([read_csv(f, sep=",", usecols = ["UniqueCarrier", "Origin"]) for f in files], keys=files)
city = pd.read_csv(path + '/flightData/airportcode.csv', sep=",", usecols = ["Name", "Code"])
airline = pd.read_csv(path + '/flightData/airlines.csv', sep=",", usecols = ["Airline", "AirlineName"])

carrierNamedata = airline.loc[airline["Airline"] == args.carrier]
indexlist = carrierNamedata.index.tolist()
carrierName = carrierNamedata.ix[indexlist[0], "AirlineName"] 
print carrierName
# get the results for specific carrier
originByCarrier = origin.loc[origin['UniqueCarrier'] == args.carrier]

originArray = origin.Origin.unique()

originCountArray = {}
for i in originArray:
    # print i
    countByOrigin = originByCarrier.loc[originByCarrier['Origin'] == i]
    # print len(countByOrigin.index)
    cityNamedata = city.loc[city["Code"] == i]
    ilist = cityNamedata.index.tolist()
    cityName = cityNamedata.ix[ilist[0], "Name"]
    originCountArray[cityName] = len(countByOrigin.index)

count = 10
print("top ten origins by " + carrierName)
citylist = []
countlist = []
for w in sorted(originCountArray, key=originCountArray.get, reverse=True):
	count -= 1

	if count < 0:
		break

	citylist.append(w)
	countlist.append(originCountArray[w])
	print w, originCountArray[w]

# create bar chart for top ten origins for specific carrier

y_pos = np.arange(len(citylist))

plt.bar(y_pos, countlist, align='edge', alpha=0.5)
plt.xticks(y_pos, citylist)
plt.ylabel('Number of flights')
plt.title('Total numbe of flights by city for ' + carrierName)
 
plt.show()

