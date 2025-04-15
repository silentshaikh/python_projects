# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

def findPerimeter():
    try:
        sideOne = float(input("Enter the length of 1 side : "))
        sideTwo = float(input("Enter the length of 2 side : "))
        sideThree = float(input("Enter the length of 3 side : "))
        print("\n ### PERIMETER OF THE TRIANGLE ### \n")
        print(f"The Perimeter of the Triangle is {sideOne+sideTwo+sideThree}")
    except :
        print("Please Enter the sides of Triangle")

findPerimeter()
