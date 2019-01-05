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
    if (" " != board[0] == board[1] == board[2]):
        return True;

def checkForWin(board):
    return (checkForWinLine(board[0]) || checkForWinLine(board[1]) || checkForWinLine(board[2]) ||
        checkForWinLine([board[0][0], board[0][1], board[0][2]]]) || checkForWinLine([board[1][0], board[1][1], board[1][2]]]) || checkForWinLine([board[2][0], board[2][1], board[2][2]]]) ||
        checkForWinLine([board[0][0], board[1][1], board[2][2]]]) || checkForWinLine([board[2][0], board[1][1], board[0][2]]]))

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




board = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]
checkForWinRow(board)

displayBoard(board)
