# Rock Paper Scissors
import random

#handle logics for game
def handleLogic(randomValue,userValue):
    if (userValue == "rock" and randomValue == "scissor") or (userValue == "scissor" and randomValue == "paper") or (userValue == "paper" and randomValue == "rock"):
        return True  

def rockPaper():
    print("\n ### WELCOME TO THE GAME ### \n")
    game_limit = 10
    game_point = 0

    #list for rock , paper , scissor
    listForGame = ["rock","paper","scissor"]
    while game_limit>0:

        getRandom = random.choice(listForGame)
        print(getRandom)
    #list of option
        print("""
  ##########            
    Rock
    Paper
    Scissor
  ##########  
""")
    # enter an option
        chooseOption = input("Enter an Option : ")
    #check if input is empty or game is tie
        if not chooseOption:
            print("\nPlease Enter an Option\n")
        elif chooseOption == getRandom:
            print("\nThe Game has Tie !\n")
    
    #check win or lose
        if handleLogic(getRandom.lower(),chooseOption.lower()):
            print("\nYou Win the Game.\n")
            game_point +=1
        else:
            print("\nYou Lose the Game\n")
            if game_point<1:
                game_point = 0
            else:
                game_point -=1
        print(f"\n Your Score is {game_point} \n")
        game_limit-=1
    
    


rockPaper()