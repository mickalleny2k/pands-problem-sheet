# Author : Michael Allen
#Week 2 Assignment
# Prompt the user and read in two money amounts (in cent)

amount1 = input ("enter amount in cents :" )
amount2 = input ("enter amount in cents :" )
total = int(amount1) + int(amount2)
print ("The sum of these is $" + str((total)/100))