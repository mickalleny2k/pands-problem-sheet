# pands-problem-sheet
Problem Sheet for Programming and Scripting module

# WEEK 1 
## Purpose of Task
Print Hello World

## Installation
Run the python program in Visual Studio Code 

# WEEK 2 
## Purpose of Task
The program should:
Prompt the user and read in two money amounts (in cent)
- Add the two amounts
- Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

## Explanation of the code step-by-step:
- import re module
- create two variables for amount1 and amount2
- Use sub function in re module
- change cents to dollars
- format the answer and print

## Research for Week 2 : 
https://realpython.com/python-sum-function/
https://stackoverflow.com/questions/2389846/python-decimals-format

# Week 3
## Purpose of Task
Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

## Installation
Run the python program accounts.py in Visual Studio or another similar application which supports Python

## Explanation of the code step-by-step:
- import math module
- User inputs a 10 digit account number via the command line  
- create a variable to measure the length of the number
- print the answer to the command line
- print X's and the last 4 digits

## Research : 
https://www.w3schools.com/python/python_lists.asp

# Week 4 Assignment
## Purpose of Task
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.

## Installation
Run the python program in Visual Studio Code

## Explanation of the code step-by-step:
- user inputs a number. Number variable created.
- create a while loop
- loop keeps going while the number is greater than 1
- if the number is divided 2 with remainder equal to zero
- print even number
- Divide by 2 and update the variable 
- else if the number is divided 2 with remainder not equal to zero
- print odd number 
- Multiply by 3 and update the variable
- 
## Research : 
https://www.w3schools.com/python/python_while_loops.asp

# Week 5 Task
## Purpose of Task
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
(You will need to search the web to find how you work out what day it is)

## Installation
Run the python program bank.py in Visual Studio Code

## Explanation of the code step-by-step:
- import datetime module
- get current datetime
- get day of week as an integer
- create a dictionary with 2 entries : weekday and weekend
- if it's a weekday
    print Sorry. Unfortunately it's a weekday.
- but if it's the weekend
    print Woohoo. It's the weekend. Party time.

## Research
https://www.w3schools.com/python/python_dictionaries.asp
https://www.w3schools.com/python/python_datetime.asp

# Week Task 6 
## Purpose of Task
Calculate the square root of a number using Newtons method

## Installation
Run the python program in Visual Studio Code

## Explanation of the code step-by-step:
- user inputs a number
- create a function using def 
- Set x equal to n at the start
- count the number of loop iterations     
- Execute Newton's formula        
- Check if answer is less than 1
- Break out of the loop if answer is less than 1
- Update root and perform another iteration if answer is greater than 1          
- return the square root and print the answer

##Research : 
https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python

# Week 7 : 
## Purpose of Task
This program reads in a text file and outputs the number of e's it contains

## Installation
Run the python program in Visual Studio Code

## Research
I got the for loop from this link :
#https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python

## ASSUMPTIONS
- I assume you want Uppercase E's and lowercase e's
- I assume the input file is in the same directory as es.py. If not, you must input the full path.
- I assume the input file contains the Roman alphabet. 
- It wouldn't work for the Chinese alphabet or other languages that don't use the Roman alphabet.
- It would work for the Vietnamese alphabet because Vietnamese uses the roman alphabet including the letter e and E.
- I assume the file isn't just full of numbers.  

## Explanation of the code step-by-step:
- Import the fileinput and re libraries
- Initialise the counter variable.Set it to zero
- Use a for loop to count the number of e's in each line of the text file
- find all of the e's in each line
- Update the variable after each iteration of the loop
- When you reach the end of the file, print the answer.

# WEEK 8 TASK : 
## Purpose of Task
Plotting a function and histogram

## Installation
Run the python program in Visual Studio Code

## Explanation of the code step-by-step:
- import numpy and matplotlib modules
- Generating random data with  1000 values,normal distribution, mean of 5 and standard deviation of 2   
- Plotting the histogram.
- show the plot  
- x and y axis points for the function plot
- plotting the function
- save the plot to a png
- show the plot

## Research :
https://stackoverflow.com/questions/25451294/best-way-to-display-seaborn-matplotlib-plots-with-a-dark-ipython-notebook-profil
https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html
