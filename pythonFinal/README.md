1. collect_data_py:
  The collect_data.py file is the file that read the flight data and get the useful columns as dataframe and write the dataframe into
  a new csv file for futher analysis. It first reads "UniqueCarrier", "Origin", "Dest" columns and write the results to a new csv file
  called carrierOriginDest.csv.

  Then it reads "Month", "DayofMonth", "DayOfWeek" columns and write the results to a new csv file called flightday.csv.
  Then it reads "Month", "UniqueCarrier", "ArrDelay", "DepDelay" columns and write the results to a new file called flightdelaybymonth.csv

  It also reads a file called airports.csv, and collect "Name" and "Code" columns and write the results to airportcode.csv

2. analysis_1.py:
  When executing this file, should run ./analysis_1.py AA. AA is the carrier code for American Airline, this is an example of what kind
  of parameter can be included when executing this file. This analysis will get total count of flights for each carrier in a year, and 
  create a bar chart for the result. This file will also get the carrier name from the parameter and create a pie chart for the percentage
  of this carrier in the whole market. 
  Result for analysis_1: 
    US
    504844
    WN
    1099321
    YV
    304764
    OH
    278099
    OO
    548109
    XE
    441470
    TZ
    19602
    UA
    500008
    DL
    506086
    EV
    273143
    F9
    90181
    FL
    237645
    HA
    52173
    MQ
    550088
    NW
    432880
    AA
    643597
    AS
    159404
    B6
    155732
    CO
    309389
    AQ
    35387
