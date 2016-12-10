#Introduction:

  This python analysis project is aimed to analyze US domestic flights in a whole year. Due to size limit on single files, I have split the original flight data into 32 small files and stored them under pythonFinal/flightData/flights file. A sample of the flights data is shown as below:
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%201.24.44%20PM.png)
  
The information in this data are dates of the flights, origin city, destination city, departure time, arrival time, departure delay, arrival delay, cancel status, etc. 

Link to the folder of the data: [GitHub](https://github.com/KurtWang818/python/tree/master/pythonFinal/flightData/flights)

I have created 7 py files for this project, the first collection_data.py file is for collecting data. It will extract useful columns from the data and save them into seperate small csv files. The analysis_1.py, analysis_2.py, analysis_3.py, analysis_4.py, analysis_5.py
are for analysis, and the ui.py file is the gui page that can make users easier to execute the analysis. 

#1. collect_data.py:

  The collect_data.py file is the file that read the flight data and get the useful columns as dataframe and write the dataframe into
  a new csv file for futher analysis. When executing this file, just run **python collect_data.py** and the useful data will be           collected and saved into csv files. 
  
  Link to the collect_data.py: [GitHub](https://github.com/KurtWang818/python/blob/master/pythonFinal/collect_data.py)
  
  It first reads "UniqueCarrier", "Origin", "Dest" columns and write the results to a new csv file
  called carrierOriginDest.csv.

  Then it reads "Month", "DayofMonth", "DayOfWeek" columns and write the results to a new csv file called flightday.csv.
  
  Then it reads "Month", "UniqueCarrier", "ArrDelay", "DepDelay" columns and write the results to a new file called                       flightdelaybymonth.csv
  
  It also reads a file called airports.csv, and collect "Name" and "Code" columns and write the results to airportcode.csv
  
  The following image includes the codes for extracting useful columns and write them into new csv files:
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%202.10.21%20PM.png)
  
  Since the size limit of the file for my github is 25mb, I have to seperate the csv files into smaller files. The following code is how   to seperate csv files. 
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%202.10.03%20PM.png)

#2. ui.py

  The ui.py file is a gui for all the analysis. Run **python ui.py** will start the ui page for this project. User can choose one of the five analysis and input the parameter. Then the corresponding analysis will be executed based on the user selection. Then the results and the image will be shown on a new window of the gui.
  
  Link to the ui.py file: [GitHub](https://github.com/KurtWang818/python/blob/master/pythonFinal/ui.py)
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%201.09.40%20PM.png)
  
  When the user chooses one of the analysis from the radio buttons, the input boxes will be filled automatically to help users understand what kind of parameter users can input for each analysis, and user can also change the parameters input based on his/her preference. 
  
  Airline codes that user can input are: **US, WN, YV, OH, OO, XE, TZ, UA, DL, EV, F9, FL, HA, MQ, NW, AA, AS, B6, CO, AQ**
  
  Month and day of week input are: **1 - 12 for month, 1 - 7 for day of week**
  
  Cities input are: **for example ATL for Atlanta, BOS for Boston, etc**
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%201.09.56%20PM.png)
  
  The code listed below is for executing the proper analysispy file and print the results on a new window of the user interface. 
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.04.39%20PM.png)
  
#3. analysis_1.py:
  
  When executing this file, should run **python analysis_1.py AA**. AA is the carrier code for American Airline, this is an example of what kind of parameter can be included when executing this file. This analysis will get total count of flights for each carrier in a year, and create a bar chart for the result. This file will also get the carrier name from the parameter and create a pie chart for the percentage of this carrier in the whole market. 
  
  Link to the analysis_1.py file: [GitHub](https://github.com/KurtWang818/python/blob/master/pythonFinal/analysis_1.py)
  
  This is the code to get unique carriers from the dataframe and count total flights for each carrier. Unique carriers and counts will be stored in lists. 
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%202.48.25%20PM.png)
  
  Then this analysis will create one bar chart for unique carriers and their total count, and one pie chart for the percentage of flights operated for the carrier that user searched for. For instance, if the user input AA, the pie chart will show the percentage of flights operated by AA in a whole year. The charts will be saved to the /pythonFinal/pythonFinalscreen folder first and then shown on the screen. 
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%202.48.51%20PM.png)
  
  If the user chooses analysis_1 and clicks on submit button, analysis_1.py file will be executed and the results will be shown on the user interface window. 
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%201.50.41%20PM.png)
  **Total number of flights by carrier**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis1.1.png)
  **Percentage of flights operated by American Airline, result will vary by what the user inputs**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis1.2.png)
    
#4. analysis_2.py:
  When executing this file, should run **python analysis_2.py ATL**. ATL is the city code for Atlanta, this is an example of what kind of parameter can be included when executing this file. This analysis will get total count of origin city and destination city, it
will also get the total number of flights for a route. And create bar chart for top ten origin city, destination city, and top ten     routes in a year. Then it will get the city from the parameter and create a bie chart of the percentage of flights for this city in a whole year. 
  
  Link to the analysis_2.py file: [GitHub](https://github.com/KurtWang818/python/blob/master/pythonFinal/analysis_2.py)
  
  The code below shows that the origin city, destinations city their corresponding counts are stored in dictionaries, then the dictinaries are sorted in descending order and values can be printed and saved. 
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.22.11%20PM.png)
  
  I have created a function to combine the origin city and the destination city and produce a route, then count the route and store the values into a dictionary, sort this dictionary and print and save the top ten routes. **This analysis will be executed for about 15 minutes, because the process for combining route takes a long time.**
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.28.37%20PM.png)
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.22.26%20PM.png)
  
  Then I will create charts for top origin city, destination city, routes, percentage of filghts from the specified city and percentage of flights landing at the specified city. Save the image and show them on the screen. 
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.23.01%20PM.png)
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.23.03%20PM.png)
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.23.14%20PM.png)
  
  After executin this analysis, the results will be shown on the new window of the user interface window. From these results, we can understand which cities are more inportant in the US.  
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.51.54%20PM.png)
  
  **Top ten routes and their total counts**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis2.1.png)
  
  **Top ten origin cities**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis2.2.png)
  
  **Top ten destination cities**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis2.3.png)
  
  **Percentage of flights from Atlanta, result will vary by what the user inputs**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis2.4.png)
  
  **Percentage of flights to Atlanta, result will vary by what the user inputs**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis2.5.png)
  
    
#5. analysis_3.py:
  When executing this file, should run **python analysis_3.py 1 1**. The first 1 is the month number (from 1 - 12), and the second 1 is the day of week (from 1 to 7). This analysis will get total count of flights by month and also day of week, and create bar chart for number of flights in each month and each day of week. Then it will get the month and day of week from the parameter and create bie charts of the percentage of flights for each month and each day of week. 
  
  Link to the analysis_3.py file: [GitHub](https://github.com/KurtWang818/python/blob/master/pythonFinal/analysis_3.py)
  
  This analysis will count total flight numbers by month and day of week and store the results into dictionaries. The it will create line charts to show the trend for flights with respect to month and day of week. This analysis will also get the percentage of flights in the specified month and day of week. 
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.45.23%20PM.png)
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.45.43%20PM.png)
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.45.57%20PM.png)
  
  The results will be shown on the screen. This analysis will tell us which month and what day will be more busy. 
  
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/Screen%20Shot%202016-12-10%20at%203.54.34%20PM.png)
  
  **Number of flights by month**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis3.1.png)
  
  **Number of flights by day of week**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis3.2.png)
  
  **Percentage of flights in January, result will vary by what the user inputs**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis3.3.png)
  
  **Percentage of flights on Mondays, result will vary by what the user inputs**
  ![alt tag](https://github.com/KurtWang818/python/blob/master/pythonFinal/images/analysis3.4.png)
  
  
#6. analysis_4.py:
  When executing this file, should run ./analysis_4.py 1 AA. The parameter 1 is the month number (from 1 - 12), and the aprameter AA is   the code for carrier. This analysis will get total count of departure and arrival delayed flights by month and calculate the           percentage of delayed flights by each month. It will create bar chart for percentge of departure and arrival delayed flights in each   month. Then it will also get the month from the parameter and create bie charts of the percentage of delayed flights over all the       delayed flights for the specific month. It also get the carrier name from the parameter and calculate percentage of delayed flghts of   this carrier.
  
  Link to the analysis_4.py file: [GitHub](https://github.com/KurtWang818/python/blob/master/pythonFinal/analysis_4.py)

#7. analysis_5.py:
  When executing this file, should run ./analysis_5.py AA. AA is the carrier code. This analysis will get total count of flights by       origin city for the specified carrier. Then it will sort the dictionary and return top ten origin cities for this carrier. This         analysis will show which city is the hub for each carrier.  
  
  Link to the analysis_5.py file: [GitHub](https://github.com/KurtWang818/python/blob/master/pythonFinal/analysis_5.py)
  
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

 
