# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

num_list = [3,4,6,12,3,4,3,5,4,3,6]
#create an object to store the count of each element of list
count_obj = {}
#Use For loop save the coun in object dynamically
for num in num_list:
    count_obj[f"{num}"] = num_list.count(num)

print(count_obj)

