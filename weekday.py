# Author : Michael Allen
# Week 5 Task

from datetime import datetime
# get current datetime
dt = datetime.now()
# get day of week as an integer
x = dt.weekday()

#create a dictionary with 2 entries
#weekday and weekend
day_of_week = {"weekday" : "Sorry. Unfortunately it's a weekday.", 
               "weekend" : "Woohoo. It's the weekend. Party time." }

if x <= 5: #if it's a weekday
    print (day_of_week["weekday"]) #print Sorry. Unfortunately it's a weekday.
else : #but if it's the weekend
    print (day_of_week["weekend"]) #print Woohoo. It's the weekend. Party time.
