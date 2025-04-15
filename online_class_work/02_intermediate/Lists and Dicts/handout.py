# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# # Print the length of the list.


# # Add 'mango' at the end of the list. 


# # Print the updated list


# def prodOne():
#     fruitList = ['apple', 'banana', 'orange', 'grape', 'pineapple']
#     print(f"Length of Fruit List : {len(fruitList)}")
#     fruitList.append("mango")
#     print("Updated List : ",fruitList)

# prodOne()



# Problem #2: Index Game
# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.


gameList = ["Sam",1,4,True,None,"Tom"]


# Access Element Function
def accessElements(ourList:list):
    try:

        input_for_index = int(input("Enter an Index : "))
        getElement = ourList[input_for_index]
        if getElement in ourList:

            return f"The Element you want to access is '{ourList[input_for_index]}'"
        else:
            return f"The Element of Index {input_for_index} is not available"
    except:
        return "Please Enter Only a Number (0-9)"




#modify Element Function
def modifyElement(ourList:list,new_value):
    try:
        indexForNewValue = int(input("Enter an Index to replace previous value to new value : "))
        previousElem = ourList[indexForNewValue]
        if previousElem in ourList:
            ourList[indexForNewValue] = new_value
            return f"\nYou have replaced SuccessFully '{previousElem}' to '{new_value}'\n"
        else:
            return f"The Element of Index {indexForNewValue} is not available, so you can't replace with anyone."
    except:
        return "Please Enter Only a Number (0-9)"


    


#Slicing Function
def slice_List(ourList,start_index,end_index):
    if start_index>len(ourList)-1 :
       return  f"Please Enter a Index ( 0 - {len(ourList)-1} )"
    else:
        return ourList[start_index:end_index]


#Game Interaction
def gameFunc():
    print("\nChoose an Option\n")
    print(" access - modify - slice \n")
    gameOption = input("Select an Option : ")
    if not gameOption:
        print("Please Enter an Option")

      # Access Section
    elif gameOption.lower() == "access":
        accessElemFunc =  accessElements(gameList)
        print(accessElemFunc)

      # Modify Section
    elif gameOption.lower() == "modify":
        new_value_to_replace = input("Enter a new Value : ").replace(" ",'')
        if not new_value_to_replace:
            print("Please Enter a New Value ")
        else:
            modifyElemFunc =  modifyElement(gameList,new_value_to_replace)
            print(modifyElemFunc)
            print(gameList)

       # Slicing Section     
    elif gameOption.lower() == "slice":
        try:
            startIndex = int(input("Enter an Starting Index : "))
            endIndex = int(input("Enter an Ending Index (but not including) : "))
            slicingList = slice_List(gameList,startIndex,endIndex)
            print("Slicing List : ",slicingList)
        except:
            print("Please Enter Only Number (0-9)")
    else:
        print("Invalid Option")

gameFunc()

         


