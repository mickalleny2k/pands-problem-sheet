#import the math module
import math

#User inputs a 10 digit account number via the command line  
account_number = input ("Please enter an 10 digit account number:")

#Slicing function as per feedback
#https://www.w3schools.com/python/ref_func_slice.asp
end = slice(6,10)
#print (account_number[end]) to test it works

#print the answer to the command line
print ("XXXXXX" + account_number[end])