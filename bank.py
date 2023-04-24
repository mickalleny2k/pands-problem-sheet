# Author : Michael Allen
#Week 2 Assignment
# Prompt the user and read in two money amounts (in cent)
import re
import decimal
import math

#create two variables for amount1 and amount2
amount1 = input ("enter amount in cents :" )
amount2 = input ("enter amount in cents :" )

#Substitute function in re module
result1 = re.sub(r'(..)(\.|$)', r'.\1', amount1)
#print(result1)
#change cents to dollars
result2 = re.sub(r'(..)(\.|$)', r'.\1', amount2)
#print(result2)
total = float(result1) + float(result2)
#format the answer and print
print(f"The sum of these is ${total:.2f}")

#research
#https://realpython.com/python-sum-function/
#https://stackoverflow.com/questions/66662279/python-shift-decimal-point-in-a-string-number
#https://pythonexamples.org/python-re-sub/#:~:text=Python%20re.sub%28%29%20Function.%20re.sub%28%29%20function%20replaces%20one%20or,function%20is.%20re.sub%28pattern%2C%20repl%2C%20string%2C%20count%3D0%2C%20flags%3D0%29%20where
