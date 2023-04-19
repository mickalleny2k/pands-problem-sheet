# Author : Michael Allen
#Week 2 Assignment
# Prompt the user and read in two money amounts (in cent)

#create two variables for amount1 and amount2
amount1 = input ("enter amount in cents :" )
amount2 = input ("enter amount in cents :" )

#create another variable total for the sum
total = int(amount1) + int(amount2)

#print the sum to the command line
print ("The sum of these is $" + str((total)/100))

# Here is an alternative solution
# amount1 = input ("enter amount in cents :" )
# amount2 = input ("enter amount in cents :" )
# total = int(amount1) + int(amount2)
# answer = str((total)/100)
# print (f"The sum of these is ${answer}" )
