# Author : Michael Allen
# Week 5 Task

from datetime import datetime
# get current datetime
dt = datetime.now()
# get day of week as an integer
x = dt.weekday()
#print('Day of a week is:', x)
#print('Datetime is:', dt)
day_of_week = {"weekday" : "Sorry. Unfortunately it's a weekday.", 
               "weekend" : "Woohoo. It's the weekend. Party time." }

if x <= 5:
    print (day_of_week["weekday"])
#elif x == 6 :
#    print (day_of_week["1"])
#elif x ==  :
#    print (day_of_week["2"])
#elif x == 3 :
#    print (day_of_week["3"])
#elif x == 4 :
#    print (day_of_week["4"])
#elif x == 5 :
#    print (day_of_week["weekend"])
else :
    print (day_of_week["weekend"])

