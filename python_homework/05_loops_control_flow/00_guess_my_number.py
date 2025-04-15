# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import math,random
gameCount = 10
randNum  = math.floor(random.random()*100+1) # generate random number from 1 to 100

# if count will zero so the game will end
while(gameCount>0):
    # take an input where can guess the number
    userNum = input("Guess a Number : ")
    if not userNum.replace(" ","") or not userNum.isnumeric():
      print("Please Enter Only a Number")
    else:
      userNum = int(userNum)
      if(userNum == randNum):
          print('Congratulations! You guessed the correct number. 🎉')
          break
      elif(userNum > randNum) :
          print('Your Number is Too High !')
      elif(userNum<randNum):
          print('Your Number is Too Low !')

    #decrement by 1 when user doesn't guess the number
    gameCount -=1
    # show the chances that user have
    print(f' Chances you have {gameCount} !')
    # if chances is zero and number is incorrect
    if userNum != randNum and gameCount < 1:
      print('You Lost the Game')