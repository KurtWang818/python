# python Assignement_2

File pythonAssignment2.py is for retrieving data and add the twitter results to a file. 
    When executing this file, it has to input four parameters, the first one is the search term
    the second and the third is the start and end date for the twitter being posted, 
    and the fourth one is the root directory to store the results.
    An example is: python ~/Downloads/pythonAssignment2.py trump 2016-10-15 2016-10-16 /Users/KurtWang/Desktop/study
    This mean that I am searching for twitter about Trump that is posted on 2016-10-15. And the root directory to store the 
    result is /Users/KurtWang/Desktop/study
    
File pythonAssignment2Analysis1.py is to analyze the average likes per twitter for a certain user's timeline. 
    When executing this file, it has to input one parameters, this is the location for the file to be analyzed. 
    In the pythonAssignment2.py file, I used an api to search for a user's timeline:
    twitter.statuses.user_timeline(screen_name=args.echo, since=args.since, until=args.until)
    For instance, if I searched for user "mrvincecarter15", then I could analyze the average likes per twitter for this user. 
    
File pythonAssignment2Analysis2.py is to analyze the average friends for user who tweet Trump and Hillary. 
    When executing this file, it has to input one parameters, this is the location for the file to be analyzed.
    In the pythonAssignment2.py file, I used an api to search for a certain term:
    twitter.search.tweets(q=args.echo, count=100, since=args.since, until=args.until)
    Fir instance, I searched for Trump and Hillary and I could calcualte the average friends for user who tweet about Trump
    and the average friends for user who tweet Hillary.
    
    
File pythonAssignment2Analysis3.py is to analyze top ten tweets regarding Trump by retweet_count. 
    When executing this file, it has to input one parameters, this is the location for the file to be analyzed.
    In the pythonAssignment2.py file, I used an api to search for a certain term:
    twitter.search.tweets(q=args.echo, count=100, since=args.since, until=args.until)
    
File pythonAssignment2Analysis4.py is to analyze average favorite_count for tweets regarding Trump and Hillary. 
    When executing this file, it has to input one parameters, this is the location for the file to be analyzed. 
    In the pythonAssignment2.py file, I used an api to search for a certain term:
    twitter.search.tweets(q=args.echo, count=100, since=args.since, until=args.until)
    Fir instance, I searched for Trump and Hillary and I could calcualte the average favorite_count for tweets about Trump
    and the average favorite_count for tweets about Hillary.
    
File pythonAssignment2Analysis5.py is to analyze top ten tweets regarding Hillary by retweet_count. 
    When executing this file, it has to input one parameters, this is the location for the file to be analyzed. 
    In the pythonAssignment2.py file, I used an api to search for a certain term:
    twitter.search.tweets(q=args.echo, count=100, since=args.since, until=args.until)
    
File pythonAssignment2Analysis6.py is to analyze top ten tweets regarding Trump by retweet_count on a certain day. 
    When executing this file, it has to input one parameters, this is the location for the file to be analyzed. 
    In the pythonAssignment2.py file, I used an api to search for a certain term:
    twitter.search.tweets(q=args.echo, count=100, since=args.since, until=args.until)
