#!/usr/bin/python

# names= ["Year","Month","DayofMonth","DayOfWeek","DepTime","CRSDepTime","ArrTime","CRSArrTime","UniqueCarrier","FlightNum","TailNum","ActualElapsedTime","CRSElapsedTime","AirTime","ArrDelay","DepDelay","Origin","Dest","Distance","TaxiIn","TaxiOut","Cancelled","CancellationCode","Diverted","CarrierDelay","WeatherDelay","NASDelay","SecurityDelay","LateAircraftDelay"]
# data = pd.read_csv('~/Downloads/2006.csv', sep=",", header = None, names= ["Year","Month","DayofMonth","DayOfWeek","DepTime","CRSDepTime","ArrTime","CRSArrTime","UniqueCarrier","FlightNum","TailNum","ActualElapsedTime","CRSElapsedTime","AirTime","ArrDelay","DepDelay","Origin","Dest","Distance","TaxiIn","TaxiOut","Cancelled","CancellationCode","Diverted","CarrierDelay","WeatherDelay","NASDelay","SecurityDelay","LateAircraftDelay"])

#read flight information and write carrier, origin city, and destination city into a csv file called carrierOriginDest.csv
import pandas as pd
from pandas import *
import glob
# data1 = pd.read_csv('~/Downloads/2006.csv', sep=",", usecols = ["UniqueCarrier", "Origin", "Dest"])
# data1.head()

# data1.to_csv('~/Downloads/flightData/carrierOriginDest.csv', sep=',', index = False)

# read all the csv files, get UniqueCarrier Origin Dest columns and concatenate into one dataframe and write the result to a csv file
files = ["~/Downloads/2006flight/2006.1.csv", "~/Downloads/2006flight/2006.2.csv", "~/Downloads/2006flight/2006.3.csv", "~/Downloads/2006flight/2006.4.csv", "~/Downloads/2006flight/2006.5.csv", "~/Downloads/2006flight/2006.6.csv", "~/Downloads/2006flight/2006.7.csv", "~/Downloads/2006flight/2006.8.csv"]
data1 = concat([read_csv(f, sep=",", usecols = ["UniqueCarrier", "Origin", "Dest"]) for f in files], keys=files)

data1.to_csv('~/Downloads/flightData/carrierOriginDest.csv', sep=',', index = False)


# data2 = pd.read_csv('~/Downloads/2006.csv', sep=",", usecols = ["Month", "DayofMonth", "DayOfWeek"])
# data2.head()

# data2.to_csv('~/Downloads/flightData/flightday.csv', sep=',', index = False)

# read all the csv files, get Month DayofMonth DayOfWeek columns and concatenate into one dataframe and write the result to a csv file
data2 = concat([read_csv(f, sep=",", usecols = ["Month", "DayofMonth", "DayOfWeek"]) for f in files], keys=files)

data2.to_csv('~/Downloads/flightData/flightday.csv', sep=',', index = False)

# data3 = pd.read_csv('~/Downloads/2006.csv', sep=",", usecols = ["Month", "UniqueCarrier", "ArrDelay", "DepDelay"])
# data3.head()

# data3.to_csv('~/Downloads/flightData/flightdelaybymonth.csv', sep=',', index = False)

# read all the csv files, get Month UniqueCarrier ArrDelay DepDelay columns and concatenate into one dataframe and write the result to a csv file
data3 = concat([read_csv(f, sep=",", usecols = ["Month", "UniqueCarrier", "ArrDelay", "DepDelay"]) for f in files], keys=files)

data3.to_csv('~/Downloads/flightData/flightdelaybymonth.csv', sep=',', index = False)


data4 = pd.read_csv('~/Downloads/pythonFinal/airports.csv', sep=",", usecols = ["Name", "Code"])
data4.head()

data4.to_csv('~/Downloads/flightData/airportcode.csv', sep=',', index = False)





