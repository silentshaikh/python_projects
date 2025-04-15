# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.


def getLastElement(list):
    if not list:
        return "list have no element"
    else:
        return list[len(list)-1]

def addElementInList():
    myList = []

    inputForElement = input("Enter a element to add in a list :")
    while inputForElement!="":
            myList.append(inputForElement)
            inputForElement = input("Enter a element to add in a list :")
    print(myList)
    return myList

print(getLastElement(addElementInList()))
