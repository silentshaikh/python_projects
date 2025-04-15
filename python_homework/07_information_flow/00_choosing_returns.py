# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

# We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead.

# Here are two sample runs of the program, one for each return option (user input in bold italics):

# (Entered age is an adult age)

# How old is this person?: 35

# True

# (Entered age is not an adult age)

# How old is this person?: 7

# False


adult_age = 18
def check_person_is_adult():
    personAge = input("Enter Your Age :")
    if not personAge.isdigit():
        print("Enter only number (0-9)")
        return False
    else:
        personAge = int(personAge)
        if personAge >= adult_age:
            return True
        else:
            return False

print(check_person_is_adult())