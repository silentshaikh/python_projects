# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

def squareOfNum():
    try:
        numForSquare = float(input("Enter a Number for show its sqaure : "))
        print(f'Square of {numForSquare} is {numForSquare**2}')
    except:
        print("Please Enter only a Number.")
squareOfNum()

    