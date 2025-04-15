# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

numbers = [1, 2, 3, 4]
def doubleList():
    return [num**2 for num in numbers]

print(f"Single List : {numbers}")
print(f"Double List : {doubleList()}")
