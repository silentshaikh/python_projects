# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2
import math
def remainderDivision():
    try:

     numOne = float(input("Enter a Number : "))
     numTwo = float(input("Enter a Number : "))
     print("\n ### REMAINDER DIVISION ### \n")
     print(f"The Result of the division is {math.trunc((numOne//numTwo))} with a remainder of {math.trunc(numOne%numTwo)}")
    except:
       print("Please Enter a Number ")

remainderDivision()
