import random

def printBoard(board):
    print(board[1] + ' |' + board[2] + '|' + board[3])
    print('--+-+--')
    print(board[4] + ' |' + board[5] + '|' + board[6])
    print('--+-+--')
    print(board[7] + ' |' + board[8] + '|' + board[9])

def selectPlayerLetter():
    letter= ' '
    while not (letter == 'X' or letter == 'O'):
        print('Select X or O as your letter')
        letter = input().upper()
    if (letter == 'X'):
        return ['X', 'O']
    else:
        return ['O', 'X']

def selectPlayerLetterForP2P():
    letter= ' '
    if random.randint(0, 1) == 0:
        print('Player 1 select your letter')
        while not (letter == 'X' or letter == 'O'):
            print('Select X or O as your letter')
            letter = input().upper()
        if (letter == 'X'):
            return ['X', 'O']
        else:
            return ['O', 'X']
    else:
        print('Player 2 select your letter')
        while not (letter == 'X' or letter == 'O'):
            print('Select X or O as your letter')
            letter = input().upper()
        if (letter == 'X'):
            return ['X', 'O']
        else:
            return ['O', 'X']

def playerSelect():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playerSelectForP2P():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'

def playAgain():
    print('Do you want to play again?, Press Y for yes and N for no')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[6] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter))

def getBoardCopy(board):
    duplicateBoard = []
    for i in board:
        duplicateBoard.append(i)
    return duplicateBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? Press any number between 1 to 9')
        move = input()
    return int(move)

def randomMoveChoice(board, moveList):
    possibleMove = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMove.append(i)
    if len(possibleMove) != 0:
        return random.choice(possibleMove)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
        if isWinner(copy, computerLetter):
            return i

    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
        if isWinner(copy, playerLetter):
            return i

    move = randomMoveChoice(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return randomMoveChoice(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print ('Welcome to Ajays Tic Tac Toe game!')

while True:
    board = [' ']*10
    print('Enter 1 for Player vs Computer and 2 for Player vs Player')
    option = int(input())
    if option == 1:
        playerLetter1, computerLetter = selectPlayerLetter()
        turn = playerSelect()
        print('The ' + turn + ' is playing first')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                printBoard(board)
                move = getPlayerMove(board)
                makeMove(board, playerLetter1, move)

                if isWinner(board, playerLetter1):
                    printBoard(board)
                    print('Hurray!Player wins the game')
                    gameIsPlaying = False
                else:
                    if isBoardFull(board):
                        printBoard(board)
                        print('The game is a tie')
                        break
                    else:
                        turn = 'computer'

            else:
                move = getComputerMove(board, computerLetter)
                makeMove(board, computerLetter, move)

                if isWinner(board, computerLetter):
                    printBoard(board)
                    print('Ohh:( Computer wins the game, play again?')
                    gameIsPlaying = False
                else:
                    if isBoardFull(board):
                        printBoard(board)
                        print('The game is a tie')
                        break
                    else:
                        turn = 'player'
        if not playAgain():
            break
    elif option == 2:
        playerLetter1, playerLetter2 = selectPlayerLetterForP2P()
        turn = playerSelectForP2P()
        print('The ' + turn + ' is playing first')
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'player1':
                printBoard(board)
                move = getPlayerMove(board)
                makeMove(board, playerLetter1, move)

                if isWinner(board, playerLetter1):
                    printBoard(board)
                    print('Player1 wins the game')
                    gameIsPlaying = False
                else:
                    if isBoardFull(board):
                        printBoard(board)
                        print('The game is a tie')
                        break
                    else:
                        turn = 'player2'

            else:
                printBoard(board)
                move = getPlayerMove(board)
                makeMove(board, playerLetter2, move)

                if isWinner(board, playerLetter2):
                    printBoard(board)
                    print('Player2 wins the game, play again?')
                    gameIsPlaying = False
                else:
                    if isBoardFull(board):
                        printBoard(board)
                        print('The game is a tie')
                        break
                    else:
                        turn = 'player1'
        if not playAgain():
            break