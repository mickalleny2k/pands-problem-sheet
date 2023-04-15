# Author : Michael Allen
# Week Task 6
# Calculate the square root of a number using Newtons method

# user inputs a number
n = input("Please input a number : ")

# create a function using def 
def square_root(n, l) :
 
    # Set x equal to n at the start
    x = n
 
    # To count the number of loop iterations
    count = 0
 
    while (1) :
        count += 1
 
        # Newton's formula
        root = 0.5 * (x + (n / x))
 
        # Check if answer is less than 1
        if (abs(root - x) < l) :
            break
            # break out of the loop if answer is less than 1

        # Update root and perform another iteration if answer is greater than 1 
        x = root
 
    return root
  
print(f"The square root of {n} is {square_root(int(n), 1)}")
 