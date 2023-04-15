# Author : Michael Allen
# The number of E's and e's in a text file
# Import the fileinput and re libraries
import fileinput
import re

#Initialise the counter variable.Set it to zero
number_of_es = 0

#https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python
#Use a for loop to count the number of e's in each line of the text file
for line in fileinput.input():
    es = len(re.findall('[Ee]', line))
    #find all of the e's in each line
    number_of_es = number_of_es + es
    # Update the variable after each iteration of the loop

print(f"The total number of E's and e's contained in the text file is {number_of_es}")