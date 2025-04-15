import random
def high_low_game():
    print("\n ### Welcome to the High-Low Game! ### \n")
    max_round = 5
    count_round = 1
    user_score = 0
    while count_round<=max_round:
        userNum = random.randint(1,100)+1
        computerNum = random.randint(1,100)+1
        print(f"\n Round {count_round}")
        print(f"Your number is {userNum}")
        userNumLowOrHigh = input("Do you think your number is higher or lower than the computer's?: ")
        if not userNumLowOrHigh:
            print("Please Enter , do you think number is higher or lower !")
        elif userNumLowOrHigh.lower() == "higher":
            if userNum>computerNum:
                print(f"You were right! The computer's number was {computerNum}")
                user_score +=1
            else:
                print(f"Aww, that's incorrect. The computer's number was {computerNum}")
                user_score -=1
        elif userNumLowOrHigh.lower() == "lower":
            if userNum<computerNum:
                print(f"You were right! The computer's number was {computerNum}")
                user_score +=1
            else:
                print(f"Aww, that's incorrect. The computer's number was {computerNum}")
                user_score -=1
        else:
            print("Please Enter higher or lower !")
        print(f"Your score is now {user_score}")
        count_round +=1
    if user_score == 5:
        print(" \n Congratulation, You guessed all number correctly ! \n")
    elif user_score == 4:
        print("\n You did very well \n")
    else:
        print("\n Try Again to acheive more points ")
    print("\n ### Thanks for playing! ### \n")

high_low_game()