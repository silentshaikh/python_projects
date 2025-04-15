# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

def set_list_of_num():
    numList = []
    while True:
        numINput = input("Enter a Number : ")
        if not numINput or not numINput.isdigit():
            print("Please Enter Only a Number")
        else:
            numINput = int(numINput)
            numList.append(numINput)
        addMore = input("do you want to add more (yes | no) : ")
        if addMore.lower() == "yes".replace(" ",''):
            continue
        else:
            break
    return numList

num_list =  set_list_of_num()
print(num_list)

def count_even(numList):
    count = 0
    for num in numList:
        if num % 2 == 0:
            count +=1
    return f"\n Total Count of Even Number is {count}"

countOfEven = count_even(num_list)
print(countOfEven)