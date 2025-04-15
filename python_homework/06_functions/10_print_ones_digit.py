# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):

# Enter a number: 42 The ones digit is 2

def print_one_digits(num):
    numInput = input("Enter a Number : ")
    if numInput.isdigit():
        return int(numInput)%10
    else:
        return "Please Enter Only a Number"


print(print_one_digits(42))
