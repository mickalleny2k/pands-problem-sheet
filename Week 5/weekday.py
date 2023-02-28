# Author : Michael Allen
# Week 5 Task

from datetime import datetime
# get current datetime
dt = datetime.now()
# get day of week as an integer
x = dt.weekday()

day_of_week = {"weekday" : "Sorry. Unfortunately it's a weekday.", 
               "weekend" : "Woohoo. It's the weekend. Party time." }

if x <= 5:
    print (day_of_week["weekday"])
else :
    print (day_of_week["weekend"])

