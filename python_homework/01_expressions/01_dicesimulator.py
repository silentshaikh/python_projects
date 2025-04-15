# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
import random

def dice_roll():
    max_num = 6
    diceOne = random.randint(1,max_num)
    diceTwo = random.randint(1,max_num)
    totalOfDice = diceOne+diceTwo
    print(f"Th Total Dice is {totalOfDice}")

def mainBox():
    diceOne = 10
    print(f"diceOne in mainBox() start as {diceOne}")
    dice_roll()
    dice_roll()
    dice_roll()
    print(f"diceOne in mainBox() is {diceOne}")

mainBox()


# gameCount = 10
# userOne = 0
# userTwo = 0
# while gameCount>=1:
#       try:
#            #take to input generate a random number
#         inputForDiceNum = int(input("Enter a Number to generate a random for the users (0-9): "))
#         diceOne = random.randint(1,inputForDiceNum)
#         diceTwo = random.randint(1,inputForDiceNum)
#         userOne += diceOne 
#         userTwo += diceTwo
#         print(f"Sam has {userOne} points.")
#         print(f"Tom has {userTwo} points.")
#       except:
#            print("Please Enter only Integer (0-9)")
#       gameCount -=1
     
# print("\n ### Now , The Winner is : ### \n")
# if userOne>userTwo:
#      print(f"Sam has {userOne} points.")
# else:
#      print(f"Tom has {userTwo} points.")
     

