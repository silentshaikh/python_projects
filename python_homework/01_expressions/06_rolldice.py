# Simulate rolling two dice, and prints results of each roll as well as the total.
import random

def rollDice():
    max_num = 6
    diceOne = random.randint(1,max_num)
    diceTwo = random.randint(1,max_num)
    print(f"Dice One : {diceOne}")
    print(f"Dice Two : {diceTwo}")
    print("\n ### Dice Rolling ### \n")
    print(f"Total Dice is {diceOne+diceTwo}")

rollDice()