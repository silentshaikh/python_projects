# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message

def main():
    numOne  = input("Enter a Number : ").replace(" ",'')
    numTwo = input("Enter a Number : ").replace(" ",'')
    try:
         numOne = float(numOne)
         numTwo = float(numTwo)
         if numOne.is_integer() or numTwo.is_integer():
            
            numOne = int(numOne)
            numTwo = int(numTwo)
            sumOfNumbers = numOne+numTwo
         else:
            sumOfNumbers = numOne+numTwo
         print("\n ### ADD TWO NUMBER ### \n")
         print(f" The Sum of {numOne} and {numTwo} is {sumOfNumbers} .")
    except ValueError:
        print("Please Enter Only a Number.")


main()