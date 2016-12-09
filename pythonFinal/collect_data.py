#!/usr/bin/python

#read flight information and write carrier, origin city, and destination city into a csv file called carrierOriginDest.csv
import pandas as pd
from pandas import *
import glob
import sys 
import os

path = os.path.split(os.path.realpath(sys.argv[0]))[0]
print path

# Define file_splitter function
def file_splitter(fullfilepath, lines=50):
  """Splits a plain text file based on line count."""
  path, filename = os.path.split(fullfilepath)
  basename, ext = os.path.splitext(filename)
 
  # Open source text file
  with open(fullfilepath, 'r') as f_in:
    try:
      # Open first output file
      f_output = os.path.join(path, '{}_{}{}'.format(basename, 0, ext))
      f_out = open(f_output, 'w')
 
      # Read input file one line at a time
      for i, line in enumerate(f_in):
        # When current line can be divided by the line
        # count close the output file and open the next one
        if i % lines == 0:
          f_out.close()
          f_output = os.path.join(path, '{}_{}{}'.format(basename, i, ext))
          f_out = open(f_output, 'w')
 
        # Write current line to output file
        f_out.write(line)
 
    finally:
      # Close last output file
      f_out.close()


# read all the csv files, get UniqueCarrier Origin Dest columns and concatenate into one dataframe and write the result to a csv file

files = [path + "/flightData/flights/2006.1.csv", path + "/flightData/flights/2006.2.csv", path + "/flightData/flights/2006.3.csv", path + "/flightData/flights/2006.4.csv", path + "/flightData/flights/2006.5.csv", path + "/flightData/flights/2006.6.csv", path + "/flightData/flights/2006.7.csv", path + "/flightData/flights/2006.8.csv", path + "/flightData/flights/2006.9.csv", path + "/flightData/flights/2006.10.csv", path + "/flightData/flights/2006.11.csv", path + "/flightData/flights/2006.12.csv", path + "/flightData/flights/2006.13.csv", path + "/flightData/flights/2006.14.csv", path + "/flightData/flights/2006.15.csv", path + "/flightData/flights/2006.16.csv", path + "/flightData/flights/2006.17.csv", path + "/flightData/flights/2006.18.csv", path + "/flightData/flights/2006.19.csv", path + "/flightData/flights/2006.20.csv", path + "/flightData/flights/2006.21.csv", path + "/flightData/flights/2006.22.csv", path + "/flightData/flights/2006.23.csv", path + "/flightData/flights/2006.24.csv", path + "/flightData/flights/2006.25.csv", path + "/flightData/flights/2006.26.csv", path + "/flightData/flights/2006.27.csv", path + "/flightData/flights/2006.28.csv", path + "/flightData/flights/2006.29.csv", path + "/flightData/flights/2006.30.csv", path + "/flightData/flights/2006.31.csv", path + "/flightData/flights/2006.32.csv"]
data1 = concat([read_csv(f, sep=",", usecols = ["UniqueCarrier", "Origin", "Dest"]) for f in files], keys=files)

data1.to_csv(path + '/flightData/carrierOriginDest.csv', sep=',', index = False)

file_splitter(path + '/flightData/carrierOriginDest.csv', 1785550)




# # read all the csv files, get Month DayofMonth DayOfWeek columns and concatenate into one dataframe and write the result to a csv file
data2 = concat([read_csv(f, sep=",", usecols = ["Month", "DayofMonth", "DayOfWeek"]) for f in files], keys=files)

data2.to_csv(path + '/flightData/flightday.csv', sep=',', index = False)

file_splitter(path + '/flightData/flightday.csv', 3570962)


# # read all the csv files, get Month UniqueCarrier ArrDelay DepDelay columns and concatenate into one dataframe and write the result to a csv file
data3 = concat([read_csv(f, sep=",", usecols = ["Month", "UniqueCarrier", "ArrDelay", "DepDelay"]) for f in files], keys=files)

data3.to_csv(path + '/flightData/flightdelaybymonth.csv', sep=',', index = False)

file_splitter(path + '/flightData/flightdelaybymonth.csv', 1428385)


# data4 = pd.read_csv(path + '/airports.csv', sep=",", usecols = ["Name", "Code"])
# data4.head()

# data4.to_csv(path + '/flightData/airportcode.csv', sep=',', index = False)

# files = ["~/Downloads/pythonFinal/flightData/flights/2006.1.csv", "~/Downloads/pythonFinal/flightData/flights/2006.2.csv", "~/Downloads/pythonFinal/flightData/flights/2006.3.csv", "~/Downloads/pythonFinal/flightData/flights/2006.4.csv", "~/Downloads/pythonFinal/flightData/flights/2006.5.csv", "~/Downloads/pythonFinal/flightData/flights/2006.6.csv", "~/Downloads/pythonFinal/flightData/flights/2006.7.csv", "~/Downloads/pythonFinal/flightData/flights/2006.8.csv", "~/Downloads/pythonFinal/flightData/flights/2006.9.csv", "~/Downloads/pythonFinal/flightData/flights/2006.10.csv", "~/Downloads/pythonFinal/flightData/flights/2006.11.csv", "~/Downloads/pythonFinal/flightData/flights/2006.12.csv", "~/Downloads/pythonFinal/flightData/flights/2006.13.csv", "~/Downloads/pythonFinal/flightData/flights/2006.14.csv", "~/Downloads/pythonFinal/flightData/flights/2006.15.csv", "~/Downloads/pythonFinal/flightData/flights/2006.16.csv", "~/Downloads/pythonFinal/flightData/flights/2006.17.csv", "~/Downloads/pythonFinal/flightData/flights/2006.18.csv", "~/Downloads/pythonFinal/flightData/flights/2006.19.csv", "~/Downloads/pythonFinal/flightData/flights/2006.20.csv", "~/Downloads/pythonFinal/flightData/flights/2006.21.csv", "~/Downloads/pythonFinal/flightData/flights/2006.22.csv", "~/Downloads/pythonFinal/flightData/flights/2006.23.csv", "~/Downloads/pythonFinal/flightData/flights/2006.24.csv", "~/Downloads/pythonFinal/flightData/flights/2006.25.csv", "~/Downloads/pythonFinal/flightData/flights/2006.26.csv", "~/Downloads/pythonFinal/flightData/flights/2006.27.csv", "~/Downloads/pythonFinal/flightData/flights/2006.28.csv", "~/Downloads/pythonFinal/flightData/flights/2006.29.csv", "~/Downloads/pythonFinal/flightData/flights/2006.30.csv", "~/Downloads/pythonFinal/flightData/flights/2006.31.csv", "~/Downloads/pythonFinal/flightData/flights/2006.32.csv"]
# data1 = pd.read_csv('~/Downloads/2006.csv', sep=",", usecols = ["UniqueCarrier", "Origin", "Dest"])
# data1.head()
# data1.to_csv('~/Downloads/flightData/carrierOriginDest.csv', sep=',', index = False)
# data2 = pd.read_csv('~/Downloads/2006.csv', sep=",", usecols = ["Month", "DayofMonth", "DayOfWeek"])
# data2.head()
# data2.to_csv('~/Downloads/flightData/flightday.csv', sep=',', index = False)
# data3 = pd.read_csv('~/Downloads/2006.csv', sep=",", usecols = ["Month", "UniqueCarrier", "ArrDelay", "DepDelay"])
# data3.head()
# data3.to_csv('~/Downloads/flightData/flightdelaybymonth.csv', sep=',', index = False)


