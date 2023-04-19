# Author : Michael Allen
#Week 4 Assignment

#import the maths module
import math
# user inputs a number. Number variable created.
number = int(input("enter an integer:"))

#create a while loop
# loop keeps going while the number is greater than 1
while number > 1:
    if (number % 2) == 0: #if the number is divided 2 with remainder equal to zero
        print (str(number) + " is an even number") #print even number
        number = number/2 # Divide by 2 and update the variable 
         
    elif (number % 2) != 0: # else if the number is divided 2 with remainder not equal to zero
        print (str(number) + " is an odd number") #print odd number
        number = (number * 3) + 1 # Multiply by 3 and update the variable
