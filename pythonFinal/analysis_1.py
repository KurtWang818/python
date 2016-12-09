#!/usr/bin/python

import argparse
import pandas as pd
from pandas import *
from matplotlib import pyplot as plt
import numpy as np
import sys 
import os

path = os.path.split(os.path.realpath(sys.argv[0]))[0]

# get the name of the carrier from the parameter 
parser = argparse.ArgumentParser(description='search for flight')
parser.add_argument("carrier", help="flight carrier")
args = parser.parse_args()

# read the carrierOriginDest.csv file and get name of carriers and total number of flights by carriers
files = [path + "/flightData/carrierOriginDest_0.csv", path + "/flightData/carrierOriginDest_1785550.csv", path + "/flightData/carrierOriginDest_3571100.csv", path + "/flightData/carrierOriginDest_5356650.csv"]
# carriers = pd.read_csv(path + '/flightData/carrierOriginDest.csv', sep=",", usecols = ["UniqueCarrier", "Origin", "Dest"])
carriers = concat([read_csv(f, sep=",", usecols = ["UniqueCarrier", "Origin", "Dest"]) for f in files], keys=files)
carrierArray = carriers.UniqueCarrier.unique()
flights = len(carriers.index)

carrierCountArray = []
for i in carrierArray:
    print i
    countByCarrier = carriers.loc[carriers['UniqueCarrier'] == i]
    print len(countByCarrier.index)
    carrierCountArray.append(len(countByCarrier.index))

# carrierCountArray.to_csv(path + '/flightData/flightday.csv', sep=',', index = False)

# create bar chart for number of flights by carrier

y_pos = np.arange(len(carrierArray))

plt.bar(y_pos, carrierCountArray, align='edge', alpha=0.5)
plt.xticks(y_pos, carrierArray)
plt.ylabel('Number of flights')
plt.title('Total numbe of flights by carrier')
 
plt.show()

# create pie chart by specific carrier
explode = (0.1, 0)
colors = ['blue', 'green']
labels = [args.carrier, 'Other carriers']
number = carriers.loc[carriers['UniqueCarrier'] == args.carrier]
number = len(number)
rest = flights - number
sizes = [number, rest]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of flights by carrier')
plt.show()
