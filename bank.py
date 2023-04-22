# Author : Michael Allen
#Week 2 Assignment
# Prompt the user and read in two money amounts (in cent)
#import re
#import decimal
#amount1 = input ("enter amount in cents :" )
#amount2 = input ("enter amount in cents :" )
#total = int(amount1) + int(amount2)
#print ("The sum of these is $" + str((total)/100))

# Here is an alternative solution
#create two variables for amount1 and amount2
amount1 = input ("enter amount in cents :" )
amount2 = input ("enter amount in cents :" )

#create another variable total for the sum
total = float(amount1) + float(amount2)

#create another variable
hundred = 100
#create another variable answer
#Divide the total by divide  to covert from cents to cents and dollars
answer = total/hundred

#print the answer to the command line
#You can use "f-strings" (f for "formatted string literals"), the short format style from Python v3.6 on
#https://stackoverflow.com/questions/2389846/python-decimals-format
print (f"The sum of these is ${answer:.2f}" )

#research
#https://realpython.com/python-sum-function/

#left_shift = 2
#split = total.split(".")
#"".join([split[0][:-left_shift], ".", split[0][-left_shift:], split[1]])
#print(split)