# Author : Michael Allen
# Week Task 6
# Calculate the square root of a number using Newtons method

# user inputs a number
n = input("Please input a positive integer : ")

# write a function that takes in a number and returns a value 
def sqrt(n) :
    # Set x equal to n at the start
    x = n
    # To count the number of loop iterations
    count = 0
    # the loop continues as long as n is greater than 1
    while (n > 1) :
        count += 1
        # Newton's formula
        root = 0.5 * (x + (n / x))
        # Check if answer is less than 1
        if (abs(root - x) < 1) :
            break
            # break out of the loop if answer is less than 1
        # Update root and perform another iteration if answer is greater than 1 
        x = root
    return float(root)

if int(n) <= 0:
    #print (" Please enter a positive integer")
    n = input("LISTEN TO ME BUDDY-) I said please input a positive integer : ")
    if int(n) <= 0:
        print("Third times a charm")
        n = input("Pretty please input a positive integer for goodness sake : ")
        if int(n) <= 0:
            print("No more chances. I give up")

#print the square root. Format the answer. One decimal point.
print(f"The square root of {n} is approx. {sqrt(float(n)):.1f}")

    

 