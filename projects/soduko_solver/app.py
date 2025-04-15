# This line defines a function named findNextEmpty, which takes one parameter: puzzle.
# puzzle is expected to be a 9×9 grid (a 2D list) representing the Sudoku board.
def findNextEmpty(puzzle):

    # This line starts a loop over all rows in the Sudoku grid.
    # r will go from 0 to 8 (9 rows total).
    for r in range(9):

        # This nested loop goes through all columns in the current row.

        # c will also go from 0 to 8 (9 columns per row).
        # Together, this nested loop visits every cell in the 9×9 board — from top-left to bottom-right.
        for c in range(9):

            # Checks if the current cell is empty.
            # In this code, -1 is used to represent an empty cell.
            # If the cell at row r, column c is empty → we found the next place to try a number.
            if puzzle[r][c] == -1:

                # If an empty cell is found, return its coordinates as a tuple (row, column).
                # For example, if the first empty cell is at row 2, column 5 → returns (2, 5).
                return r,c
    
    #  If no empty cell is found after scanning the entire board, return (None, None).
    # This means the board is completely filled, and it's a signal to the solver that the puzzle might be solved.
    return None, None


# Defines a function named isValid that takes:

# puzzle: the Sudoku board (a 2D list).
# guess: the number you want to try placing (from 1 to 9).
# row, column: the location in the board where you're trying to place the guess.
def isValid(puzzle,guess,row,column):

    # Gets all the values in the specified row of the board.
    # Example: if row = 3, this gets the entire 4th row (indexing starts at 0).
    rowVals = puzzle[row]

    # Checks if your guess is already present in that row.
    #  If the number already exists in the row → it's invalid → return False.
    if guess in rowVals:
        return False
    
    # This loop creates a list of all values in the specified column by picking the same column from all rows.
    # puzzle[i][column] means: "get the value in the column from each row i".
    colVals = []

    for i in range(9):
        colVals.append(puzzle[i][column])
    
    # This line replaces the loop above with a cleaner version using list comprehension.
    # You can remove the for loop above it — this line does the same thing more efficiently.
    # colVals = [puzzle[i][column] for i in range(9)]

    # Checks if your guess is already present in the column.
    #  If yes → invalid → return False.
    if guess in colVals:
        return False
    
    # Calculates the starting row and column of the 3×3 subgrid that the cell belongs to.

    #  Explanation:
        # row // 3 gives 0, 1, or 2 depending on which group of 3 rows it's in.
        # Multiplying by 3 gives the top-left corner of that box.
        #  For example:
        # If row = 4, column = 7, this will set rowStart = 3, colStart = 6, which is the top-left corner of that 3×3 box.
    rowStart = (row // 3)*3
    colStart = (column // 3)*3

    # Loops through the 3×3 box starting at (rowStart, colStart).
    # If guess is already present in any cell in that box → return False.
    # This makes sure that number appears only once per box
    for r in range(rowStart,rowStart+3):
        for c in range(colStart,colStart+3):
            if puzzle[r][c]  == guess:
                return False
    
    #  If the guess passed all 3 checks (row, column, and box), it’s a valid move → return True.
    return True

#  -----------------------------------------------------------------------------------


# This function takes the Sudoku board (puzzle) as input and tries to solve it using recursion and backtracking.
def solveSudoko(puzzle):

    #  Calls findNextEmpty(puzzle) to get the row and column of the first empty cell (where value is -1).
        # Returns:
        # (row, col) if an empty cell is found
        # (None, None) if the board is already ful
    sodRow, sodColumn  = findNextEmpty(puzzle)

    # If no empty cells are left, then the puzzle is solved → return True.
    if sodRow is None:
        return True

    # This loop tries all numbers from 1 to 9 as a possible guess for the empty cell.
    # This is where trial and error happens — trying one number at a time.
    for guess in range(1,10):

        # Calls isValid() to check:
        # Is it safe to place this guess at that cell?
        # Does it break Sudoku rules?
        # If it’s valid → go ahead!
        if isValid(puzzle,guess,sodRow,sodColumn):

            # Places the guess in the empty cell — tentatively.
            # This is a trial step. We will undo it (backtrack) if it doesn’t lead to a solution.
            puzzle[sodRow][sodColumn] = guess
            
            #  Recursively calls solveSudoko again with the updated board.
            # If the rest of the board can be solved with this guess → return True.
            # If this path leads to a solution, we’re done!
            if solveSudoko(puzzle):
                return True
        #  If the guess didn’t work out (i.e., it didn’t lead to a valid solution), we reset the cell back to -1.
        # This is backtracking — we "undo" the guess and try the next number.
        puzzle[sodRow][sodColumn] = -1
    
    #  If none of the guesses (1–9) work for this empty cell, return False.
    # This tells the previous recursive call: "Hey, this path didn’t work out, backtrack again."
    return False
# ----------------------------------------------------------------------------------------------------


#  This is your Sudoku puzzle.
#    It's a 9x9 grid.
#    -1 represents an empty cell.

# Each list inside example_board is a row.
example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]


# This calls your solveSudoko() function with example_board as the argument.

#  What it does:

# Tries to solve the puzzle using the backtracking method we discussed.

# It modifies example_board in-place (directly).

# It returns True if solved successfully, otherwise False.

# So this print() will show either:

# True → puzzle solved

# False → no solution exists
print(solveSudoko(example_board))


# This prints the final state of the board, after solving it.
#  If solveSudoko() worked correctly, you'll see a fully filled 9x9 Sudoku grid (with no -1s left and valid Sudoku rules).
print(example_board)