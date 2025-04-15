# we imported Human Class and Computer Class from player.py file
from player import HumanPlayer,RandomComputerPLayer,GeniusComputerPlayer

# This defines the TicTacToe class, which is a blueprint for creating Tic-Tac-Toe game objects. These objects will handle the board state and the logic of the game.
class TicTacToe:

    #this is a constructer , it will call when we create an instance if this class
    def __init__(self):

        # This line creates a list with 9 elements, all initialized as " ", which represents an empty spot on the TicTacToe board. The range(9) creates a sequence of 9 numbers (from 0 to 8), and for each iteration, we append a " " (empty space) to the list. This list will represent the TicTacToe grid.
        self.board = [" " for _ in range(9)]

        # This sets the current_winner attribute to None initially. This attribute will be used later to track if there is a winner in the game. If a player wins, this variable will be set to the player's letter (either "X" or "O").
        self.current_winner = None

    # It is responsible for printing the current state of the TicTacToe board.
    def print_board(self):

        # This line creates a loop that iterates over the board and breaks it into 3 rows. The board has 9 elements, so the slice self.board[i*3:(i+1)*3] extracts 3 elements from the board at a time.

        # i*3 gives the starting index for each row (e.g., for i=0, it starts at index 0, for i=1, it starts at index 3).
        # (i+1)*3 gives the ending index (e.g., for i=0, it goes up to index 3).

        for row in (self.board[i*3:(i+1)*3] for i in range(3)):

            # For each row, the elements are joined by " | " (which is the separator between cells in the TicTacToe board). The " | " is added at the start and end to make it look like a standard TicTacToe board.
            print("| " + " | ".join(row) + " |")


    @staticmethod

    # This function is used to print a "numbered" version of the board. This helps players know which spot corresponds to each index of the self.board list.
    def print_board_nums():

        # This is a list comprehension that generates a 2D list representing numbers for each spot on the board.

        # The outer loop (for j in range(3)) iterates over the 3 rows of the board.
        # The inner list comprehension ([str(i) for i in range(j*3, (j+1)*3)]) creates a list of numbers in the range j*3 to (j+1)*3, converting each number to a string. This creates numbers from 0 to 8, mapping the board positions.
        num_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        # print(num_board)

        # This loop prints each row of the numbered board, with the numbers joined by " | " as separators.
        for row in num_board:
            print("| "+" | ".join(row) + " |")

    # This method returns a list of available (empty) spots on the board.
    def available_moves(self):

        # This is a list comprehension that loops over each spot in self.board and checks if it is empty (' ').

        # enumerate(self.board) returns both the index (i) and the value (spot) of each element in the board.
        # The condition if spot == ' ' checks if the current spot is empty.
        # If the spot is empty, the index i is added to the resulting list
        return [i for i,spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     if spot == "":
        #         moves.append(i)
        # return moves

    
    #  This method checks if there are any empty squares on the board.
    def empty_squares(self):

        # This checks if the string " " (an empty square) exists in the self.board list. If there is any empty space, it returns True, otherwise False.
        return " " in self.board
    
    # This method returns the count of empty squares on the board.
    def num_empty_squares(self):

        # The .count(" ") method counts how many times " " appears in the self.board list, which tells us how many empty spots there are.
        return self.board.count(" ")
    

    # This method is responsible for making a move on the board. It takes in square (the position where the move is being made) and letter (either "X" or "O").
    def make_move(self,square,letter):

        # This checks if the selected square is empty. If it's not empty, the move cannot be made.
        if self.board[square] == " ":

            # If the square is empty, this line places the letter (either "X" or "O") in that square.
            self.board[square] = letter

            # This checks if the current player has won by making the move. The winner method is used to determine if the move has created a winning combination.
            if self.winner(square,letter):
                # If a winner is found, the current_winner is set to the player's letter.
                self.current_winner = letter
            # The move is valid and successfully made, so the method returns True.
            return True
        # If the square was already occupied, the method returns False
        return False
    

    #  This method checks if a player has won after making a move at a specific square with the given letter.
    def winner(self,square,letter):

        #  This calculates the row index for the given square.
        row_ind = square // 3

        # This extracts the row of the TicTacToe board that contains the square
        row = self.board[row_ind*3: (row_ind+1)*3]

        # This checks if all the spots in the row are filled with the letter (meaning the row is completely filled by the current player). If true, the player has won via the row.
        if all([spot == letter for spot in row]):
            return True
        
        # This calculates the column index for the given square.
        col_ind = square % 3

        # This constructs the column by looping through the board and selecting the correct elements based on the column index.
        column = [self.board[col_ind+i*3] for i in range(3)]

        # This checks if the column is completely filled with the letter.
        if all([spot == letter for spot in column]):
            return True
        
        # This condition checks if the square is on a diagonal (since diagonals are formed by positions 0, 4, 8 or 2, 4, 6).
        if square % 2 == 0:

            # This defines the first diagonal, which contains the spots at indices 0, 4, and 8.
            diagonal_1 = [self.board[i] for i in [0,4,8]]
            
            # This checks if the first diagonal is fully filled with the letter.
            if all([spot == letter for spot in diagonal_1]):
                return True
            
            # This defines the second diagonal, which contains the spots at indices 2, 4, and 6.
            diagonal_2  = [self.board[i] for i in [2,4,6]]

            # This checks if the second diagonal is fully filled with the letter.
            if all([spot == letter for spot in diagonal_2]):
                return True
        #  If no winning condition is met, the method returns False.
        return False
    

# This is the function definition for playGame. It takes 4 parameters:

# game: The instance of the TicTacToe class, representing the game state.
# xPlayer: An instance of a player class (likely HumanPlayer or RandomComputerPlayer), representing the "X" player.
# oPlayer: An instance of a player class representing the "O" player.
# printGame: A boolean flag to control whether the game board and moves should be printed during the game. It's set to True by default.
def playGame(game,xPlayer,oPlayer,printGame=True):

    # This checks if printGame is True. If so, it prints the numbered TicTacToe board using game.print_board_nums(). This board shows numbers from 0 to 8, representing each square on the grid.
    if printGame:
        game.print_board_nums()
    
    # Initializes the letter variable to "X", meaning that the "X" player starts the game.
    letter  = "X"

    # This starts a while loop that continues as long as there are empty squares on the board. The loop will end when there are no more empty squares (game.empty_squares() returns False).
    while game.empty_squares():

        # This checks if it's the "O" player's turn (letter == "O").
        # If it's the "O" player's turn, the get_move method is called for the oPlayer instance, passing the current game state (game), and the returned square is where the "O" player wants to place their mark.
        if letter == "O":
            square = oPlayer.get_move(game)
        else:

        # If it's not the "O" player's turn, then it's the "X" player's turn.
        # The get_move method is called for the xPlayer instance, passing the current game state, and the returned square is where the "X" player wants to place their mark.
            square = xPlayer.get_move(game)


        # This calls the make_move method on the game instance, passing in the square the player selected and the player's letter ("X" or "O").
        # If the move is successful (i.e., the square was empty and the move was valid), it returns True.
        if game.make_move(square,letter):

            #If the move was successful and printGame is True, it prints:
            # The move made by the current player ({letter} makes a move to square {square}).
            # The updated board is printed using game.print_board().
            # An empty line (print("")) for separation.
            if printGame:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print("")

            # This checks if the current player has won by making this move (game.current_winner).
            # If there is a winner, it prints a message indicating the winning player ({letter} wins) and returns the winning player's letter ("X" or "O").

            # The return letter statement ends the function and indicates the winner.
            if game.current_winner:
                if printGame:
                    print(f"{letter} wins")
                return letter
            # This switches the turn to the other player by changing the letter. If it's "X"'s turn, it switches to "O", and vice versa.
            letter = "O" if letter == "X" else "X"
    # If the loop finishes (meaning the board is full and there is no winner), it prints "It's a Tie" if printGame is True.
    if printGame:
        print("It's a Tie")



# This checks if the script is being run directly (not imported as a module).
# If the script is being run directly, the following block of code will execute.
if __name__ == "__main__":
    xWin = 0
    oWin = 0
    ties = 0
    xPlayer = HumanPlayer("X")
    oPlayer = GeniusComputerPlayer("O")
    tic = TicTacToe()
    result = playGame(tic,xPlayer,oPlayer,printGame=True)
    if result == "X":
        xWin +=1
    elif result == "O":
        oWin +=1
    else:
        ties +=1
    print(f"After 1000 iterations, we see {xWin} X-wins, {oWin} O wins, {ties} ties")
