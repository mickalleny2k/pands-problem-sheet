#import the math module
import math

#User inputs a 10 digit account number via the command line  
account_number = input ("Please enter an 10 digit account number:")

#create a variable to measure the length of the number
account_length = len(account_number)

#create a variable to measure the number of X's
number_of_xs = (account_length - 4) * "X"

#print the answer to the command line
#print X's and the last 4 digits
print (number_of_xs + account_number[-4:])