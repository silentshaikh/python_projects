# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

# Here's a sample run of the program (user input is in blue):

# Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)

# Note that you can call input() with no prompt and it will still wait for a user to type something!

my_affirmation = "I am capable of doing anything I put my mind to."

def affirmation_func():
    print(f"\n Print the Following affirmation : {my_affirmation} . \n")
    userInput = input().strip()
    while userInput.lower() != my_affirmation.lower():
        print("That's wasn't affirmation !")
        # ask the user to type affimation again
        print(f"\n Print the Following affirmation : {my_affirmation} . \n")
        userInput = input()
    print("That's right! :)")


affirmation_func()

