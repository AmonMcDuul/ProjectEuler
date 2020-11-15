# Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.
# p096_1.png     p096_2.png
# A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.
# The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).
# By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
] 

def loadPuzzle():
    """
    A method to read a file having puzzle in it. The puzzle should have nine lines
     of nine numbers each between 0-9 seprated by commas.
     
    Arguments:
    None
    
    Output:
    A list variable board
    """
    board = []
    fileHandle = open("sudokutest.txt", "r")
    puzzle = fileHandle.readlines()
    for line in range(len(puzzle)):
        if line != len(puzzle) - 1:
            puzzle[line] = puzzle[line][:-1]
            board.append(list(map(int,puzzle[line].split(","))))
        else:
            board.append(list(map(int,puzzle[line].split(","))))
    fileHandle.close()
    return board

def findEmpty(board):
    """
    A method to find the next empty cell of the puzzle.
    Iterates from left to right and top to bottom
    
    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list
    
    Output:
    A tuple (i, j) which is index of row, column
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #row, column
    return None

def valid(board, num, pos):
    """
    A method to find if a number num is valid or not
    
    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list
    num - a number between 1 to 9 both inclusive
    pos - a tuple (i, j) representing row, column
    
    Output:
    True if the number is valid in position pos of puzzle else False.
    """
    row = pos[0]
    column = pos[1]    #checking rows
    for i in range(len(board[0])):
        if board[row][i] == num and column != i:
            return False    #checking columns
    for i in range(len(board)):
        if board[i][column] == num and row != i:
            return False
    
    #checking box
    startRowBox = row//3 
    startColumnBox= column//3
    for i in range(startRowBox*3, (startRowBox*3)+3):
        for j in range(startColumnBox*3, (startColumnBox*3)+3):
            if board[i][j] == num and row != i and column != j:
                return False
    return True

def printBoard(board):
    """
    A method to print the sudoku puzzle in a visually appealing format
    
    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list
    
    Output:
    Prints a nine x nine puzzle represented as a sudoku puzzle. Returns None.
    """
    if not findEmpty(board):
        print("Finished puzzle")
    else:
        print("Unsolved puzzle")
    for i in range(len(board)):
        if i%3 == 0:
            print("-------------------")
            
        for j in range(len(board[0])):
            if j%3 == 0:
                print("\b|", end ="")
            
            print(str(board[i][j])+" ", end="")
        print("\b|")
    print("-------------------")

def solve(board):
    """
    A method to solve the sudoku puzzle using the other functions defined.
    We use a simple recursion and backtracking method.
    
    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list
    
    Output:
    Returns True once the puzzle is successfully solved else False
    """
    find = findEmpty(board)
    
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(board, i, find):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
    return False

# board = loadPuzzle()   #loading the board from puzzle file     
printBoard(board)      #printing the board before solving the puzzle
solve(board)           #solving the puzzle
printBoard(board)      #printing the puzzle after solving