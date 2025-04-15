import random,math

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



# A new class GeniusComputerPlayer that inherits from a base Player class.
# It represents a very smart player that uses the Minimax algorithm to make unbeatable moves.
class GeniusComputerPlayer(Player):

    # It takes letter ("X" or "O") to know which symbol this player uses.
    def __init__(self, letter):

        # calls the __init__ of the Player base class to initialize the letter.
        super().__init__(letter)
    

    # This function is called whenever the AI needs to make a move.
    def get_move(self,game):

    # If it's the first move of the game (all 9 spots are free), the AI picks a random square — this speeds things up (Minimax isn't necessary yet).
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:

            # Otherwise, it calls the minimax() function to find the best possible move
            square = self.minimax(game,self.letter)["position"]
        return square
    
    # This is the core of the AI — a recursive function to simulate all possible game outcomes and choose the best move.
    def minimax(self,state,player):

        # maxPlayer is the AI itself (X or O).
        # otherPlayer is whoever the opponent is (human or another AI).
        maxPlayer = self.letter
        otherPlayer = "O" if player == "X" else "X"

        # If the opponent just won, it means this is a bad move for the current player.
        if state.current_winner == otherPlayer:

            # The score is calculated:
            # If otherPlayer is AI, score is positive → good.
            # If otherPlayer is the human, score is negative → bad.
            # We add +1 to the score for earlier wins (faster wins are better, slower losses are better).
            return {
                "position":None,
                "score":1*(state.num_empty_squares()+1) if otherPlayer == maxPlayer else -1 * (
                    state.num_empty_squares() + 1)
                    }
        
        # This checks if the board is full and there's no winner → it’s a tie.
        # In that case, return score 0.
        elif not state.empty_squares():
            return {"position":None,"score":0}
        
        # We set a best dictionary to track the best move and score.
        # If it’s the AI's turn, we want to maximize the score, so we start from negative infinity.
        # If it’s the opponent’s turn, we want to minimize the score, so we start from positive infinity.
        if player == maxPlayer:
            best = {"position":None,"score":-math.inf}
        else:
            best = {"position":None,"score":math.inf}
        
        # Loop through every available square on the board.
        for possibleMove in state.available_moves():

            # Try making the move on that square as the current player.
            state.make_move(possibleMove,player)

            # Recursively call minimax again but switch the player (simulate opponent's move).
            sim_score = self.minimax(state,otherPlayer)

            # After the simulation, undo the move so we can try the next possibility.
            state.board[possibleMove] = " "

            # Also reset the current_winner because it may have been updated.
            state.current_winner = None

            # Store the move that led to this simulation. This helps us choose the best move.
            sim_score["position"] = possibleMove

            # If it's AI’s turn, we want the highest score.
            # If it’s the opponent’s turn, we want the lowest score (to simulate worst-case).
            if player == maxPlayer:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                 if sim_score["score"] < best["score"]:
                    best = sim_score
        # After checking all possible moves, return the best move and score found.
        return best
    
