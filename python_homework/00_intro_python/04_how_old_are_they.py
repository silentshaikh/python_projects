# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

def ageRelatedRiddle():
    anton = 21
    beth = 6 + anton
    chen = 20 + beth
    drew = chen+anton
    ethan = chen
    #store frind age
    friendAge = {
        "Anton": anton,
        "Beth": beth,
        "Chen": chen,
        "Drew": drew,
        "Ethan": ethan
    }
    for key,value in friendAge.items():
        print(f"{key} age is {value} .")

ageRelatedRiddle()
