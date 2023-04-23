# Author : Michael Allen
# The number of E's and e's in a text file
# Import the fileinput and re libraries
# ASSUMPTIONS
# I assume you want Uppercase E's and lowercase e's
# I assume the input file is in the same directory as es.py. If not, you must input the full path.
# I assume the input file contains the Roman alphabet. 
# It wouldn't work for the Chinese alphabet or other languages that don't use the Roman alphabet.
# It would work for the Vietnamese alphabet because Vietnamese uses the roman alphabet including the letter e and E.
# I assume the file isn't full of numbers 

import fileinput
import re

#Initialise the counter variable.Set it to zero
number_of_es = 0

#Research
#https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python
#Use a for loop to count the number of e's in each line of the text file
for line in fileinput.input():
    es = len(re.findall('[Ee]', line))
    #find all of the e's and E's in each line
    number_of_es = number_of_es + es
    # Update the variable after each iteration of the loop

print(f"The total number of E's and e's contained in the text file is {number_of_es}")