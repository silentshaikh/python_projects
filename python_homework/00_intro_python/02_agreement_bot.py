# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):
# What's your favorite animal? cow
# My favorite animal is also cow!

def favouriteAnimal():
    userInput = input("Enter Your Favoutirte Animal : ")
    if not userInput:
        print("Please Enter Your Favourite Animal")
    else:
        print(f"My Favourite Animal is \033[1m\033[3m {userInput}\033[0m")
favouriteAnimal()
