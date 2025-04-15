# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

# To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

# Asks the user for their first name and stores it in a variable

# Asks the user for their last name and stores it in a variable

# Asks the user for their email address and stores it in a variable

# Returns all three of these pieces of data in the order it was asked

# You can return multiple pieces of data by separating each piece with a comma in the return line.

# Here is an example run of the program:

# What is your first name?: Jane

# What is your last name?: Stanford

# What is your email address?: janestanford@stanford.edu

# Received the following user data: ('Jane', 'Stanford', 'janestanford@stanford.edu')

# (Note. This idea is called tuple packing/unpacking. We "pack" our return values into a single data structure called a tuple. We can then "unpack" these values back into our original values or leave them as a tuple.)
import re

def register_user():
    firstName = input("Enter Your First Name : ")
    lastName = input("Enter Your Last Name : ")
    userEmail = input("Enter Your Email : ")
    if not firstName or not lastName or not userEmail:
        print("Please Enter your name and email.")
        return None
    else:
        if len(firstName) < 3 or len(lastName) < 3:
            print("Please Enter your name with atleast 3 Characters.")
        if not re.match(r"^[a-zA-Z0-9\_\.\%\+\-]+\@[a-zA-Z0-9\.\-]+\.[a-z]{2,7}$",userEmail):
            print("Please Enter a Correct Email.")
        if (len(firstName) > 3 and len(lastName) > 3) and re.match(r"^[a-zA-Z0-9\_\.\%\+\-]+\@[a-zA-Z0-9\.\-]+\.[a-z]{2,7}$",userEmail):
            print("\n ### CONGRATULATION ### \n")
            print("Your Account has Created SuccessFully \n")
            return firstName,lastName,userEmail

registerData = register_user()

def print_user_data(data):
    print("\n The Recieving Data is : \n")
    print(data)

print_user_data(registerData)