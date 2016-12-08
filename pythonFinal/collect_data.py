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
files = ["~/Downloads/pythonFinal/flightData/flights/2006.1.csv", "~/Downloads/pythonFinal/flightData/flights/2006.2.csv", "~/Downloads/pythonFinal/flightData/flights/2006.3.csv", "~/Downloads/pythonFinal/flightData/flights/2006.4.csv", "~/Downloads/pythonFinal/flightData/flights/2006.5.csv", "~/Downloads/pythonFinal/flightData/flights/2006.6.csv", "~/Downloads/pythonFinal/flightData/flights/2006.7.csv", "~/Downloads/pythonFinal/flightData/flights/2006.8.csv", "~/Downloads/pythonFinal/flightData/flights/2006.9.csv", "~/Downloads/pythonFinal/flightData/flights/2006.10.csv", "~/Downloads/pythonFinal/flightData/flights/2006.11.csv", "~/Downloads/pythonFinal/flightData/flights/2006.12.csv", "~/Downloads/pythonFinal/flightData/flights/2006.13.csv", "~/Downloads/pythonFinal/flightData/flights/2006.14.csv", "~/Downloads/pythonFinal/flightData/flights/2006.15.csv", "~/Downloads/pythonFinal/flightData/flights/2006.16.csv", "~/Downloads/pythonFinal/flightData/flights/2006.17.csv", "~/Downloads/pythonFinal/flightData/flights/2006.18.csv", "~/Downloads/pythonFinal/flightData/flights/2006.19.csv", "~/Downloads/pythonFinal/flightData/flights/2006.20.csv", "~/Downloads/pythonFinal/flightData/flights/2006.21.csv", "~/Downloads/pythonFinal/flightData/flights/2006.22.csv", "~/Downloads/pythonFinal/flightData/flights/2006.23.csv", "~/Downloads/pythonFinal/flightData/flights/2006.24.csv", "~/Downloads/pythonFinal/flightData/flights/2006.25.csv", "~/Downloads/pythonFinal/flightData/flights/2006.26.csv", "~/Downloads/pythonFinal/flightData/flights/2006.27.csv", "~/Downloads/pythonFinal/flightData/flights/2006.28.csv", "~/Downloads/pythonFinal/flightData/flights/2006.29.csv", "~/Downloads/pythonFinal/flightData/flights/2006.30.csv", "~/Downloads/pythonFinal/flightData/flights/2006.31.csv", "~/Downloads/pythonFinal/flightData/flights/2006.32.csv"]
data1 = concat([read_csv(f, sep=",", usecols = ["UniqueCarrier", "Origin", "Dest"]) for f in files], keys=files)

data1.to_csv('~/Downloads/pythonFinal/flightData/carrierOriginDest.csv', sep=',', index = False)


# data2 = pd.read_csv('~/Downloads/2006.csv', sep=",", usecols = ["Month", "DayofMonth", "DayOfWeek"])
# data2.head()

# data2.to_csv('~/Downloads/flightData/flightday.csv', sep=',', index = False)

# read all the csv files, get Month DayofMonth DayOfWeek columns and concatenate into one dataframe and write the result to a csv file
# data2 = concat([read_csv(f, sep=",", usecols = ["Month", "DayofMonth", "DayOfWeek"]) for f in files], keys=files)

# data2.to_csv('~/Downloads/flightData/flightday.csv', sep=',', index = False)

# data3 = pd.read_csv('~/Downloads/2006.csv', sep=",", usecols = ["Month", "UniqueCarrier", "ArrDelay", "DepDelay"])
# data3.head()

# data3.to_csv('~/Downloads/flightData/flightdelaybymonth.csv', sep=',', index = False)

# read all the csv files, get Month UniqueCarrier ArrDelay DepDelay columns and concatenate into one dataframe and write the result to a csv file
# data3 = concat([read_csv(f, sep=",", usecols = ["Month", "UniqueCarrier", "ArrDelay", "DepDelay"]) for f in files], keys=files)

# data3.to_csv('~/Downloads/flightData/flightdelaybymonth.csv', sep=',', index = False)


# data4 = pd.read_csv('~/Downloads/pythonFinal/airports.csv', sep=",", usecols = ["Name", "Code"])
# data4.head()

# data4.to_csv('~/Downloads/flightData/airportcode.csv', sep=',', index = False)





