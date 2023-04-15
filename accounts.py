# Task for Week 3 accounts.py
# Author : Michael Allen
import math
account_number = input ("Please enter an 10 digit account number:")
account_length = len(account_number)
#print (account_length)
#print ((account_length) - 4)
#print (((account_length) - 4) * "X")
print ((((account_length) - 4) * "X")  + account_number[-4:])