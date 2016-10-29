The queryStackExchange.py is the file to query the stack exchange api. When executing this file, it has to send the directory as a parameter to store the json results. 
For example: python queryStackExchange.py ~/Desktop/study
It will create a directory called stackApi and a file called stackOutput.json 
to store 600 json results of questions with tags python and pandas from the stackOverflow website. 

The stackExchangeAnalysis1.py file analyze the total number of badges for each user. When executing this file, it has to send the directory as a parameter to store the json results. 
For example: python stackExchangeAnalysis1.py ~/Desktop/study
It will read the ~/Desktop/study/stackApi/stackOutput.json file and loop every json result. It will get the userId and use userId to request for user details. And also create a json file called stackUserOutput.json to store all the user details. And then calculate the user badge number and sort questions by badge number. 

The stackExchangeAnalysis2.py file analyze the total number of each badge for each user. When executing this file, it has to send the directory as a parameter for where the json file exists. 
For example: python stackExchangeAnalysis2.py ~/Desktop/study
It will read the ~/Desktop/study/stackApi/stackUserOutput.json file
and get number of gold. silver, bronze badge for each user. If the number is greater than 0, it will put in the dictonary. Then it will sort all the three dictionaries, and will show the user with most gold, silver, bronze badges. And also calculate how many users have gold, silver, and bronze badges. 

The stackExchangeAnalysis3.py file analyze number of answers for each question, number of questions asked for each tag, and total number of answers for each tag, it has to send the directory as a parameter for where the json file exists. 
For example: python stackExchangeAnalysis3.py ~/Desktop/study
It will also sort the question by number of answers. Sort tags with number of questions asked. Sort tags with number of answers. 

The stackExchangeAnalysis4.py file analyze user by reputation, it has to send the directory as a parameter for where the json file exists. 
For example: python stackExchangeAnalysis4.py ~/Desktop/study
It will sort user by number of reputations. 

The stackExchangeAnalysis5.py file analyze questions by score, it has to send the directory as a parameter for where the json file exists. 
For example: python stackExchangeAnalysis5.py ~/Desktop/study
It will sort questions by score.