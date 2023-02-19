import math
number = int(input("enter an integer:"))
while number > 1:
    if (number % 2) == 0:
        print (str(number) + " is an even number")
        number = number/2
         
    elif (number % 2) != 0:
        print (str(number) + " is an odd number")
        number = (number * 3) + 1