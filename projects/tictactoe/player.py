import random

# This defines a base class named Player.
class Player:
    #  the constructor method that runs when a new Player object is created.
    def __init__(self,letter):
        
        self.letter = letter # The symbol the player will use in the game — usually "X" or "O".

    # This is a method that any subclass of Player must implement
    def get_move(self,game):
        # game -> This parameter refers to the current TicTacToe game object. It will let us check the board and available moves.
        pass

# A new class called RandomComputerPlayer, and it inherits from the base Player class.
class RandomComputerPLayer(Player):
    # This is the constructor. It’s called when we create a new computer player.
    def __init__(self, letter):
        # This calls the __init__ method of the parent (Player) class.
        super().__init__(letter)
       # letter -> The same "X" or "O" like before — tells us what letter this computer player is playing as.

    # This method decides which move the computer will make
    def get_move(self,game):

        #game -> It gives the method access to the current game state (like which squares are free).

        # game.available_moves() gives us a list of all empty squares (like [0, 3, 4]).
        # random.choice(...) picks one random square from the list.
        square = random.choice(game.available_moves())
        return square
 
# A new class called HumanPlayer, which inherits from the base Player class.
class HumanPlayer(Player):

    # This is the constructor. It’s called when we create a new player.
    def __init__(self, letter):

        # This calls the __init__ method of the parent (Player) class.
        super().__init__(letter)

    # This is where the real player chooses their move.
    def get_move(self, game):

        # We set this flag to False initially to enter the while loop.
        valid_square = False

        # Just creating a placeholder variable for the player's move.
        val = None

        # Keep looping until the user enters a valid move
        while not valid_square:

            # Ask the human player to input a number (0 to 8).
            square = input(self.letter+"turns .Input moves (0-8):")
            try:
                # Convert the input value from string to integer.
                val = int(square)
                # We check if the move is legal (square is empty).
                # If it's not, we raise a ValueError.
                if val not in game.available_moves():

                    # Forces the program to jump to the except block.
                    raise ValueError
                
                valid_square = True
            except ValueError :
                print('Invalid Square')
            print(game.available_moves()) 
        #once the palyer enter a valid mode we return it
        return val
