import random

def drawBoard(board):
    # This function prints out the board that was passed

    # 'board' is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    # This will allow the player to select which team they want to be x or o
    # Return a list with the player's letter as the first item and the computer's as the second

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    # Randomly select who gets the first turn
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a players letter, this function returns True if that player has won
    # bo is short for board, and le for letter. This is to reduce the amount of typing needed
    return ((bo[7] == le and bo[8] == le and bo[9] == le)) 
    (bo[4] == le and bo[5] == le and bo[6] == le)
    (bo[1] == le and bo[2] == le and bo[3] == le)
    (bo[7] == le and bo[4] == le and bo[1] == le)
    (bo[8] == le and bo[5] == le and bo[2] == le)
    (bo[9] == le and bo[6] == le and bo[3] == le)
    (bo[7] == le and bo[5] == le and bo[3] == le)
    (bo[9] == le and bo[5] == le and bo[1] == le)

def getBoardCopy(board):
    # Make a copy of the board list and return it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Return true if the passed move is free on the board
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player enter their move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not 
        isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the board
    # Returns None if there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

        # Here is the algorithm for the Tic-Tac-Toe AI: