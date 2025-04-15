import random,re

# This defines a class called Board that handles all logic and representation for the Minesweeper game board.
class Board:

    # This is the constructor (initializer) for the board.

    # dimSize: The board will be dimSize x dimSize (e.g. 10x10 if dimSize = 10).
    # numBombs: Number of bombs to randomly place on the board
    def __init__(self,dimSize,numBombs):
        # These store the size and number of bombs.
        self.dimSize = dimSize
        self.numBombs = numBombs

        # alls a method to generate the board and randomly plant bombs.
        self.board = self.make_new_board()

        # After placing bombs, this sets the number of neighboring bombs on each non-bomb cell
        self.assignValueToBoard()

        # Keeps track of all locations the user has "dug" (clicked or opened).
        self.dug = set()

    # This method creates a new board and randomly plants bombs.
    def make_new_board(self):

        # Makes a 2D grid filled with None. Example for 10x10:
        # [[None, None, None,None,None,None, None, None,None,None], [None, None, None,None, None, None,None,None,None,None]]
        board = [[None for _ in range(self.dimSize)] for _ in range(self.dimSize)]

        # Counter to keep track of how many bombs have been placed.
        bomd_planted = 0

        # Loop continues until you've placed all bombs        
        while bomd_planted<self.numBombs:
            
            # Picks a random integer between 0 and total number of cells - 1.
            # For example: if dimSize = 3, total cells = 9 → random.randint(0, 8)
            loc = random.randint(0,self.dimSize**2-1)

            row = loc // self.dimSize
            # col = loc % self.dimSize
            # Example:

            # loc = 5, dimSize = 3

            # row = 5 // 3 = 1

            # col = 5 % 3 = 2

            # So → (1, 2)

            # ✅ This tells you exactly where to place the bomb in 2D form.
            row = loc // self.dimSize
            col = loc % self.dimSize

            # If a bomb is already there, skip and retry.
            if board[row][col] == "*":
                continue

            # Places the bomb at the calculated location.
            board[row][col] = "*"

            # Increases the count.
            bomd_planted +=1
        
        #return the board after planting the bombs in a board 

        # this method lays the foundation for your Minesweeper game:

        # It builds the grid.

        # Randomizes bomb locations every game.

        # Avoids placing multiple bombs in the same cell. 
        return board 


    # This function is part of your Minesweeper game's logic, and its job is to calculate how many bombs are surrounding each non-bomb cell on your 10x10 board and assign those values to those cells.

    # Final Goal of This Function on a 10x10 Board
        # It scans each of the 100 cells, and:

        # If it's a bomb → skips it.

        # If it's not a bomb → counts how many bombs are around it and stores that number in the cell.
    def assignValueToBoard(self):

        #  (Assuming dimSize = 10)

        # This loop goes through all the rows in the board.
        # Since dimSize = 10, it will loop r = 0 to 9 (10 rows).
        for r in range(self.dimSize):

            # Inside each row, it loops through all the columns.
            # c = 0 to 9 (10 columns).
            # So in total, this nested loop will visit all 100 cells in the 10x10 grid:
            for c in range(self.dimSize):

                # If the current cell is a bomb, don’t assign a number — just skip it.
                # This protects your bomb markers (*) from being overwritten by accident.
                if self.board[r][c] == "*":
                    continue

                # For all other cells (non-bombs), this calls another method:
                #  getNumNeighbouringBomb(r, c)
                #  Which counts how many bombs are around this cell (max: 8 neighbors).

                self.board[r][c] = self.getNumNeighbouringBomb(r,c)
                # Let’s say we are at this section of a 10x10 board:
                        # [*,  , *]
                        # [ ,  ,  ]
                        # [ , *,  ]
                # Let’s focus on the center cell (1,1).
                # It is not a bomb (" ").
                # So it will check all 8 surrounding cells.

                # Surrounding cells:
                    # (0,0) → *

                    # (0,1) → empty

                    # (0,2) → *

                    # (1,0) → empty

                    # (1,2) → empty

                    # (2,0) → empty

                    # (2,1) → *

                    # (2,2) → empty

                # Total bombs around it: 3

    

    # This function is a key part of Minesweeper — it tells you how many bombs are around a given cell.
    # r: row index of the current cell (like 3)
    # c: column index of the current cell (like 4)
    # return -> The number of bombs around that cell (not including the cell itself)
    def getNumNeighbouringBomb(self,r,c):
        # Start a counter at zero
        # This will store the number of bombs we find around the cell (r, c)
        numNeighbouringBomb = 0

        # This loops from one row above to one row below the current cell.
            # Example (in a 10x10 board):

            # If r = 3, the row loop goes from 2 to 4.

            # But if r = 0 (top row), r-1 = -1 — invalid!

            # So max(0, r-1) keeps us inside the board.

            # min(self.dimSize - 1, r+1) avoids going out of bounds at the bottom.
        for row in range(max(0,r-1),min(self.dimSize-1,r+1)+1):

            #same
            for col in range(max(0,c-1),min(self.dimSize-1,c+1)+1):

                # You don’t want to count the cell (r, c) itself — just its 8 neighbors.
                # So if we’re at the same row and col, skip.
                if row == r and col == c:
                    continue

                # If the neighboring cell contains "*", it's a bomb.
                # So we increment our counter.
                if self.board[row][col] == "*":
                    numNeighbouringBomb +=1
        
        # Once we've checked all neighbors, return how many bombs were found around (r, c).
        return numNeighbouringBomb
        # getNumNeighbouringBomb(3, 4)
        # Will loop over the 8 surrounding cells, skip the center (3,4), and find:

        # (2,4) = bomb → +1

        # (3,3) = bomb → +1

        # (4,5) = bomb → +1

        # So it returns: 3
 # -------------------------------------------------------------------------------------------------------


    # dig 
    # It’s a function (a block of code) that tries to uncover a specific cell in the Minesweeper board.
    # You "dig" in a cell like you're digging in the ground to check if there’s a bomb or a safe number.
    # In real Minesweeper games, when you click a cell, it’s like “digging” into it.    

    # dug
    # This is a Python set (a collection) that stores all the cells the player has already dug.
    # This helps avoid digging the same cell again. Like a memory: "Hey, I’ve already dug here!"


    def dig(self,row,col):

        # You are saying: “I have already dug this spot.” This helps avoid rechecking the same cell
        self.dug.add((row,col))

        # If the player digs into a bomb (*), game over. We return False.
        if self.board[row][col] == "*":
            return False
        
        # If there are bombs nearby (like 1, 2, or 3 around this cell), we return True, and stop here. This means: “You're safe, but be careful!”
        elif self.board[row][col] > 0:
            return True
        
        
            #  What it's doing:
            # It's looping through all neighboring rows around the current row.

            # That means: the row above, the current row, and the row below.

            #  Example:
            # If row = 5, and board is 10×10:

            # row - 1 = 4

            # row + 1 = 6

            # max(0, 4) = 4 → ensures we don’t go above 0

            # min(9, 6) = 6 → ensures we don’t go beyond the board (dimSize - 1 = 9)

            # So range(4, 7) will loop through rows: 4, 5, and 6.
        for r in range(max(0,row-1),min(self.dimSize-1,row+1)+1):

            # same logic like row but work for column 
            for c in range(max(0,col-1),min(self.dimSize-1,col+1)+1):

                # It's skipping any cell you've already dug before.
                # We don’t want to repeat work or create infinite loops.
                if (r,c) in self.dug:
                    continue

                # What it's doing:
                # If a neighboring cell hasn’t been dug yet, call the same dig() function on it.

                # This is recursion — the function is calling itself to dig around neighbors.

                #  Example:
                # If cell (5,3) was a 0, it would dig all 8 neighbors.
                # And if any of those neighbors are also 0, it keeps going, like a chain reaction.
                self.dig(r,c)
        return True
        #Recap
        # Goes through every cell around your current location.
        # Makes sure you stay inside the board boundaries.
        # If the neighbor hasn’t been dug yet, it digs it.
        # And if that one is also empty (0), it digs its neighbors, and so on.
    #------------------------------------------------------------------------------------------------------


    # This __str__ method is all about displaying the Minesweeper board in a nice, readable format — like a grid — when you print the board object.
    def __str__(self):

        # Makes a 2D list (visibleBoard) that mirrors the size of the game board.
        # Initially fills it with None — this is where we'll store visible values (only the dug ones).
        visibleBoard = [[None for _ in range(self.dimSize)] for _ in range(self.dimSize)]

        # Loops through each cell on the board.
        # If the cell has been dug, show its value (bomb *, number, or 0).
        # Otherwise, show a blank " " (not dug yet).
        for row in range(self.dimSize):
            for col in range(self.dimSize):
                if (row, col) in self.dug:
                 visibleBoard[row][col] = str(self.board[row][col])
                else:
                    visibleBoard[row][col] = " "

        # It will hold the final board string to return.
        string_rep = ""

        # It stores the max width of each column for formatting (so grid looks neat)
        widths = []


        # For each column index:
        # Use map to extract that column across all rows.

        # Find the longest string in that column.

        # Store its length in widths. ✅ This helps align columns properly (e.g., if one cell has "10" and others have "1").
        for idx in range(self.dimSize):
            columns = map(lambda x: x[idx], visibleBoard)
            widths.append(len(max(columns, key=len)))


        # This creates a list of column numbers.

        # If self.dimSize = 10, then this will give:
        # indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # These will be displayed at the top of the board to label the column
        indices = [i for i in range(self.dimSize)]

        # Starts the string that will hold the column header row.
        # " " adds 3 spaces at the beginning to make space for the row numbers that appear on the left of the board later.
        indices_row = "   "

        # Creates an empty list to store formatted column numbers as strings.
        # Each one will be adjusted to match the correct width of its column (important for nice alignment).
        cells = []


        # Loops through each column index and value.
        # idx: position in the list (0, 1, 2, ...)
        # col: the column number itself (also 0, 1, 2, ...)
        for idx, col in enumerate(indices):

            # This creates a formatting string that says:
            # Left-align (%-)
            # Width equal to widths[idx] (the widest cell in that column).
            # String type (s).
            # So if a column's max width is 2, the format string becomes "%-2s".
            # Example: If widths = [1, 2, 2, 1, ...], then:
            # For column 0: format_str = "%-1s"
            # For column 1: format_str = "%-2s" → ensures even spacing under the numbers.
            format_str = "%-" + str(widths[idx]) + "s"

            # Formats the column number (like 0, 1, 2) using format_str and adds it to the cells list.
            # Ensures proper spacing so everything aligns under the header.
            cells.append(format_str % col)


        # Joins all the formatted column numbers from cells with double spaces (" ") between them.
        # Appends the whole line to indices_row.
        indices_row += "  ".join(cells)
        # Adds a newline (\n) to move to the next line after the column headers
        indices_row += "\n"

        # You're adding the column numbers row (which we built earlier) to string_rep.
        # string_rep is the full board string that will be returned when the board is printed.
        # At this point, string_rep looks like this:

        #    0  1  2  3  4  5  6  7  8  9
        string_rep += indices_row


        # " "
        # Adds 3 spaces at the beginning — this aligns with the left margin where the row numbers will appear (just like we did earlier).

        # "-" * (len(indices_row) - 3)
        # This adds a horizontal line separator right under the column numbers.
        # len(indices_row) is the length of the entire top row (including spaces and column numbers).
        # We subtract 3 because we already manually added " " spaces at the start — so this makes the dashes line up perfectly under the numbers.
        string_rep += "   " + "-" * (len(indices_row) - 3) + "\n"


        # Looping through each row index i in the board.
        # Since your board is 10×10, visibleBoard has 10 rows, so this loop will run 10 times (from 0 to 9).
        for i in range(len(visibleBoard)):

            # Grab the actual row (a list of strings like ["1", " ", "*", ...]) at index i from visibleBoard.
            row = visibleBoard[i]

            #  Start building the string for this row:
            # Add the row number (e.g. 0, 1, 2) on the left.
            # Followed by " |" to match the table format visually.
            string_rep += f"{i} |"

            #  Create an empty list cells to store each formatted cell value for this row.
            cells = []

            # Loop through each column cell in the row.
            # idx = index of the column (0 to 9).
            # col = content of the cell (like " ", "*", or a number as a string).
            for idx, col in enumerate(row):

                # Build a format string that ensures each cell is spaced correctly
                # Let’s say widths[idx] = 2, then:
                # format_str = "%-2s"
                # It means:
                # ➡️ Left-align the string within 2 character spaces.
                # This keeps all columns aligned even if their content varies in length.
                format_str = "%-" + str(widths[idx]) + "s"

                # Format the cell value (col) and add it to cells list.
                # For example, if col = "*", and format_str = "%-2s", it becomes "* " — so it takes up equal space like other cells.
                cells.append(format_str % col)

            # Join all formatted cell values with " |" separator and add them to string_rep.
            string_rep += " |".join(cells)

            # Close the row with " |" and add a newline to start the next row.
            string_rep += " |\n"

        # After all rows are added, draw a bottom border (just like the top one).
        string_rep += "   " + "-" * (len(indices_row) - 3)
        # Done! Return the fully built board string
        return string_rep
    # -------------------------------------------------------------------------------------------------------





# This defines the main function to play Minesweeper.
# dimSize=10 → board will be 10x10 by default.
# numBombs=10 → there will be 10 bombs randomly placed.
def play_minsweeper(dimSize=10,numBombs=10):

    # Creates a new game board object using your custom Board class.
    # This will:

    # Generate the board.

    # Randomly place bombs.

    # Set up all values (like neighboring bomb counts).
    gameBoard= Board(dimSize,numBombs)


    #  This loop keeps running until all non-bomb squares are dug.
        # gameBoard.dug is a set that tracks the cells you've revealed.
        # You win when you've dug all safe cells (i.e., total cells - number of bombs).
    while len(gameBoard.dug) < gameBoard.dimSize**2 - numBombs:

        # Prints the current state of the board (only revealed cells).
        print(gameBoard)


        #  Asks the player to input the cell they want to dig (like 3,4).
            # re.split(",(\\s)*", ...) splits input by comma and optional spaces.
            # Then int(...) turns the strings into numbers.
            # Example: "3, 4" → row = 3, col = 4
        try:
            userINput = re.split(",(\\s)*",input("Where would you like to dig ? INput as row ,col : "))
            row,col = int(userINput[0]),int(userINput[-1])

        # If the input is invalid (like missing comma, or not numbers), it shows an error and restarts the loop.
        except:
            print("\n❌ Invalid input format. Try again like this → 3,4\n")
            continue


        # Checks if the selected row/col is out of bounds of the board.
        #  If someone enters 10,10 on a 10x10 board → it's invalid because the last valid index is 9.
        if row < 0 or row >= gameBoard.dimSize or col < 0 or col >= dimSize:
            print("\n❌ Invalid location , Try Again\n")
            continue


        # Digs the selected cell:

        # If it's a bomb → returns False.
        # If it's a number → reveals just that cell.
        # If it's zero → auto-reveals neighboring cells recursively.
        safe = gameBoard.dig(row,col)

        #  If the dug cell is a bomb (safe = False) → break out of the loop -> Game Over
        if not safe:
            break
    
    # If you escaped the loop without hitting a bomb, you win!
    if safe:
        print("\n Congratulation!!!, You are Victorious \n")

    #  You lost (hit a bomb).
    else:
        print("\n Sorry Game Over \n")

        # This reveals everything on the board by force:
        # Sets dug to include all cells, even bombs.
        # This helps show the full board after a loss.
        gameBoard.dug = set((r,c) for r in range(gameBoard.dimSize) for c in range(gameBoard.dimSize))

        # Print the final board so the player can see where the bombs were.
        print(gameBoard)

# Calls the function to start the game.
play_minsweeper()


