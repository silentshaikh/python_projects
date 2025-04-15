# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

# Here's a sample run of the program (user input is in bold italics):

# Enter the length of AB: 3

# Enter the length of AC: 4

# The length of BC (the hypotenuse) is: 5.0
import math
def pythagoraos_theorem():
    try:

        ab = float(input("Enter the length of AB : "))
        ac = float(input("Enter the length of AC : "))
        ac = (ab**2) + (ac**2)
        ac = math.sqrt(ac)
        print("\n ### HYPHOTHENIS ### \n")
        print(f"The Length of BC : {ac}")
    except:
        print("Please Enter a Number")

pythagoraos_theorem()
