# Write a function that takes two numbers and finds the average between the two
from inspect import signature
def findAverage(one,two,argumentCount):
    return (one+two) / argumentCount

# find the parameters via signature
signatureForArg = signature(findAverage).parameters
#convert it into dictionary
convertIntoDict = dict(signatureForArg)
#remove the last key-value pair
convertIntoDict.popitem()
print(convertIntoDict)
#get the length of this dictionary which is 2 because we had three argument and after delete the last , we have only 2 . That what we want !
countOfArgument = len(convertIntoDict)
print(countOfArgument)
#then passed it into function argument to average 
average_of_two_number = findAverage(5,5,countOfArgument)
print(average_of_two_number)
