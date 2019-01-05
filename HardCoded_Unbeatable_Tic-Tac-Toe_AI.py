def displayBoard(board):
    for x in range(len(board)):
        line = ""
        for y in range(len(board[0])):
            line += board[x][y]
            if (y != len(board[0]) - 1):
                line += "|"
        print(line)
        if (x != len(board) - 1):
            print("-----")

def checkForWinLine(line):
    if (" " != line[0] == line[1] == line[2]):
        return True;

def checkForWin(board):
    return (checkForWinLine(board[0]) or
            checkForWinLine(board[1]) or
            checkForWinLine(board[2]) or
            checkForWinLine([board[0][0], board[1][0], board[2][0]]) or
            checkForWinLine([board[0][1], board[1][1], board[2][1]]) or
            checkForWinLine([board[0][2], board[1][2], board[2][2]]) or
            checkForWinLine([board[0][0], board[1][1], board[2][2]]) or
            checkForWinLine([board[2][0], board[1][1], board[0][2]]))

def checkForTie(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if (board[x][y] == " "):
                return False
    return True;

def checkBoard(board):
    if (checkForWin(board)):
        return "game won"
    elif (checkForTie(board)):
        return "tie"
    else:
        return "continue game"

def userTurn(board):
    num = int(input("Where would you like to move? ")) - 1
    board[int(num / 3)][num % 3] = "X"
    displayBoard(board)

def aiTurn(board):
    return ""

def gamePlay(board):
    userTurn(board);
    while(checkBoard(board) == "continue game"):
        aiTurn(board)
        userTurn(board);
    print(checkBoard(board))

board = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]
gamePlay(board)
