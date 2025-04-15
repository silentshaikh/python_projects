# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

def getFirstElement(list):
    if not list:
        return "list have no element"
    else:
        return list[0]

def addElementInList():
    myList = []

    inputForElement = input("Enter a element to add in a list :")
    while inputForElement!="":
            myList.append(inputForElement)
            inputForElement = input("Enter a element to add in a list :")
    print(myList)
    return myList

print(getFirstElement(addElementInList()))





