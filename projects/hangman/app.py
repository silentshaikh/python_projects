from wordlist import wordList
import random

#validate the word
def validate_word():
    word = random.choice(wordList)
    if "-" in word or " " in word:
        word = random.choice(wordList)
    return word.upper()

#display a hangman
stages = [
        '''
           -----
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        '''
    ]
def display_hangman(incorrect_guesses):
    """
    Returns the hangman ASCII art corresponding to the number of incorrect guesses.
    """
    global stages
    return stages[incorrect_guesses]


def hangMan():
    playMore = ""
    while playMore != "no":

        selected_word = validate_word()
        showWord = ["_"]*len(selected_word)
        print(showWord)
        used_letter = set()
        # user_selected:set = set()
        wrongGuess = 0
        # how many chances you have if you are guess wrong
        attempt_max = len(stages)-1
        while wrongGuess<=attempt_max and "_" in showWord:
            guessWord = input("Enter a Character : ").upper().replace(" ",'')
            if not  guessWord.isalpha() and not len(guessWord) == 1:
             print("Please Enter only one character")
             continue
            if guessWord in used_letter:
                print("You already guess that !")
                continue
            used_letter.add(guessWord)

            if guessWord in selected_word:
                for key,value in enumerate(selected_word):
                    if value == guessWord:
                        showWord[key] = guessWord
                print(display_hangman(wrongGuess-1))
            else:
                print(display_hangman(wrongGuess))
                print(f"Incorrect guess. You have {attempt_max - wrongGuess} attempts left.")
                wrongGuess +=1
        
            
            print(' '.join(showWord))
            print(showWord)
            print("\n")

        if '_' not in showWord:
            print("\n Congratulations! You've guessed the word! \n")
        else:
            print(f"Game over! The word was {selected_word}. Better luck next time.")
        playMore = input("Do you want to play again (yes | no) :")
        if playMore.lower() == "no":
            break
        else:
            continue
    


hangMan()
