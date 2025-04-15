# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

# For example, using a hash function called SHA256(...) something as simple as

# hello

# can be hashed into a much more complex

# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.

# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)
from hashlib import sha256

# pasword in has values for safety
def convertIntoHash(password):
    return sha256(password.encode()).hexdigest()

def registerUser():
    print("\n ### WELCOME TO REGISTER PAGE ### \n")
    userData = {}
    while True:
        userEmail = input("Enter Your Email : ")
        userPassword = input("Enter Your Password : ")
        if  not userEmail or not userPassword:
            print("Please Enter your email and password")
        else:
            userData[userEmail] = convertIntoHash(userPassword)
            addMore = input("Do you want to add more (yes | no) :")
            if addMore.lower() == "yes":
                continue
            else:
                break
    return userData

user_data = registerUser()
print(user_data)

# Now , Do Login Operation
def login_operation(login_data):
    print("\n ### WELCOME TO LOGIN PAGE ### \n")
    loginEmail = input("Enter Your Email to Login into your account : ")
    loginPassword = input("Enter Your Password to Login into your account : ")
    if not loginEmail or not loginPassword:
        print("Please Enter your email and password to login into your account")
    else:
        if login_data[loginEmail] == convertIntoHash(loginPassword):
            print("\n ### CONGRATULATION ### \n")
            print("You have successfully logged-in to your account.")
        else:
            print("Your Email or Password is Wrong.")



login_operation(user_data)
