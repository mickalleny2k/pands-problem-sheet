# Author : Michael Allen
# Week 5 Task

from datetime import datetime
# get current datetime
dt = datetime.now()
# get day of week as an integer
x = dt.weekday()
#print('Day of a week is:', x)
#print('Datetime is:', dt)
day_of_week = {"0" : "Oh No. Monday is a weekday", "1" : "Oh No. Tuesday is a weekday", "2" : "Oh No. Wednesday is a weekday",
           "3" : "Oh No. Thursday is a weekday", "4" : "Oh No. Friday is a weekday", 
           "Saturday" : "Woohoo. Saturday is the weekend", "6" : "Woohoo. Sunday is the weekend" }

if x == 0:
    print (day_of_week["0"])
elif x == 1 :
    print (day_of_week["1"])
elif x == 2 :
    print (day_of_week["2"])
elif x == 3 :
    print (day_of_week["3"])
elif x == 4 :
    print (day_of_week["4"])
elif x == 5 :
    print (day_of_week["5"])
elif x == 6 :
    print (day_of_week["6"])

