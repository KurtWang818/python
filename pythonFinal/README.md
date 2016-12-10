Introduction:
  This python analysis project is aimed to analyze US domestic flights in a whole year. Due to size limit on single files, I have split the original flight data into 32 small files and stored them under pythonFinal/flightData/flights file. A sample of the flights data is shown as below:
  ![alt tag]("~/Desktop/Screen Shot 2016-12-10 at 1.24.44 PM")

1. collect_data_py:
  The collect_data.py file is the file that read the flight data and get the useful columns as dataframe and write the dataframe into
  a new csv file for futher analysis. It first reads "UniqueCarrier", "Origin", "Dest" columns and write the results to a new csv file
  called carrierOriginDest.csv.

  Then it reads "Month", "DayofMonth", "DayOfWeek" columns and write the results to a new csv file called flightday.csv.
  Then it reads "Month", "UniqueCarrier", "ArrDelay", "DepDelay" columns and write the results to a new file called                       flightdelaybymonth.csv

  It also reads a file called airports.csv, and collect "Name" and "Code" columns and write the results to airportcode.csv

2. ui.py
  The ui.py file is a gui for all the analysis. User can choose one of the five analysis and input the parameter. Then the corresponding analysis will be executed based on the user selection. Then the results and the image will be shown on a new window of the gui.
  
3. analysis_1.py:
  When executing this file, should run ./analysis_1.py AA. AA is the carrier code for American Airline, this is an example of what kind
  of parameter can be included when executing this file. This analysis will get total count of flights for each carrier in a year, and 
  create a bar chart for the result. This file will also get the carrier name from the parameter and create a pie chart for the           percentage of this carrier in the whole market. 
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
    
4. analysis_2.py:
  When executing this file, should run ./analysis_2.py ATL. ATL is the city code for Atlanta, this is an example of what kind of         parameter can be included when executing this file. This analysis will get total count of origin city and destination city, it
  will also get the total number of flights for a route. And create bar chart for top ten origin city, destination city, and top ten     routes in a year. Then it will get the city from the parameter and create a bie chart of the percentage of flights for this city. 
  Result for analysis_2:
    **************************************************
    top origin city and count
    ATL 407971
    ORD 373736
    DFW 301163
    LAX 233788
    DEN 232476
    IAH 224061
    PHX 215086
    LAS 184733
    EWR 158291
    SLC 142080
    **************************************************
    top destination city and count
    ATL 404829
    ORD 373799
    DFW 301312
    LAX 233900
    DEN 232365
    IAH 224004
    PHX 215085
    LAS 184716
    EWR 158256
    SLC 142262
    ***************************************************
    top origin city and count
    SAN->LAX 14594
    LAX->SAN 14554
    OGG->HNL 13956
    HNL->OGG 13898
    LAX->LAS 13547
    LAS->LAX 13122
    LGA->BOS 12398
    BOS->LGA 12370
    DCA->LGA 12043
    LGA->DCA 12042
    
5. analysis_3.py:
  When executing this file, should run ./analysis_3.py 1 1. The first 1 is the month number (from 1 - 12), and the second 1 is the day   of week (from 1 to 7). This analysis will get total count of flights by month and also day of week, and create bar chart for number     of flights in each month and each day of week. Then it will get the month and day of week from the parameter and create bie charts of   the percentage of flights for each month and each day of week. 
  Result for analysis_3:
    flight by month and count
    January
    581287
    February
    531247
    March
    605217
    April
    585351
    May
    602919
    June
    598315
    July
    621244
    August
    628732
    September
    584937
    October
    611718
    November
    586197
    December
    604758
    **************************************************
    flight by day of week and count
    Monday
    1048054
    Tuesday
    1030322
    Wednesday
    1042952
    Thursday
    1052949
    Friday
    1056606
    Saturday
    899531
    Sunday
    1011508
    
6. analysis_4.py:
  When executing this file, should run ./analysis_4.py 1 AA. The parameter 1 is the month number (from 1 - 12), and the aprameter AA is   the code for carrier. This analysis will get total count of departure and arrival delayed flights by month and calculate the           percentage of delayed flights by each month. It will create bar chart for percentge of departure and arrival delayed flights in each   month. Then it will also get the month from the parameter and create bie charts of the percentage of delayed flights over all the       delayed flights for the specific month. It also get the carrier name from the parameter and calculate percentage of delayed flghts of   this carrier.
  Result for analysis_4:
    flight by month and count
    January
    581287
    February
    531247
    March
    605217
    April
    585351
    May
    602919
    June
    598315
    July
    621244
    August
    628732
    September
    584937
    October
    611718
    November
    586197
    December
    604758
    ************************************
    delay flights by month and count
    January
    197789
    February
    198371
    March
    235207
    April
    212412
    May
    218097
    June
    263900
    July
    281457
    August
    254405
    September
    209985
    October
    248878
    November
    230224
    December
    274930
    ****************************
    depart delay percentage by month
    January
    0.340260490945
    February
    0.373406343942
    March
    0.388632507018
    April
    0.362879708073
    May
    0.361735158454
    June
    0.441072010563
    July
    0.453053872552
    August
    0.404631862224
    September
    0.358987378128
    October
    0.406850869191
    November
    0.392741689227
    December
    0.454611596705
    ****************************
    arrive delay percentage by month
    January
    0.401082425721
    February
    0.439552599826
    March
    0.45071271957
    April
    0.427239382866
    May
    0.426310997
    June
    0.481047608701
    July
    0.466513962308
    August
    0.440916002367
    September
    0.435689655467
    October
    0.483925599704
    November
    0.439393241521
    December
    0.47541826648

    ************************************
    delayed flights by carrier
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
    US
    234091
    WN
    438407
    YV
    126322
    OH
    126515
    OO
    244739
    XE
    198574
    TZ
    10487
    UA
    223589
    DL
    227362
    EV
    144822
    F9
    41896
    FL
    107232
    HA
    12779
    MQ
    248671
    NW
    212232
    AA
    283476
    AS
    77465
    B6
    73500
    CO
    154532
    AQ
    10675
    ******************************
    percentage of delayed flights by carrier
    US
    0.463689773475
    WN
    0.398797985302
    YV
    0.414491212873
    OH
    0.454927921352
    OO
    0.446515200444
    XE
    0.449801798537
    TZ
    0.534996428936
    UA
    0.447170845266
    DL
    0.449255660105
    EV
    0.530205789641
    F9
    0.464576795556
    FL
    0.451227671527
    HA
    0.244935119698
    MQ
    0.452056761827
    NW
    0.490279061172
    AA
    0.440455751037
    AS
    0.48596647512
    B6
    0.471964657232
    CO
    0.499474771243
    AQ
    0.301664453048

7. analysis_5.py:
  When executing this file, should run ./analysis_5.py AA. AA is the carrier code. This analysis will get total count of flights by       origin city for the specified carrier. Then it will sort the dictionary and return top ten origin cities for this carrier. This         analysis will show which city is the hub for each carrier.  
  Result for analysis_5:
    top ten origins by American Airlines
    Dallas-Fort Worth 163509
    Miami 40878
    Los Angeles 31038
    New York 22230
    St. Louis 20602
    San Juan 13991
    Boston 13136
    San Francisco 12770
    Orlando 11517
    Austin 9341

 
