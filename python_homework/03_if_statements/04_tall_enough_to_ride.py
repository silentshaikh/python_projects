# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

# Here's two sample runs (user input is in bold italics):

# How tall are you? 100

# You're tall enough to ride!

# How tall are you? 10

# You're not tall enough to ride, but maybe next year!

# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this? See the function tall_enough_extension() in the solution code!)

def tallEnough():
    try:
        min_height = 4.5
        max_height = 8
        userHeight = float(input("Enter you height in feet : "))
        if userHeight>=min_height and userHeight<=max_height:
            print("\n ### CONGRATULATION ### \n")
            print("You are tall enough to ride !")
        else:
            print("You are not tall enough to ride !")
    except:
        print("Please Enter only Number")

tallEnough()
