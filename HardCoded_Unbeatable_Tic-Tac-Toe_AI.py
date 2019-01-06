import random
import os

def displayBoard(board):
    clear = lambda: os.system('cls')
#    clear()
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

def checkForPossibleWinLine(line, char):
    if ((line[0] == line[1] == char or line [0] == line[2] == char or line[1] == line[2] == char) and (line[0] == " " or line[1] == " " or line[2] == " ")):
        if (line[0] == " "):
            return 0
        elif(line[1] == " "):
            return 1
        elif(line[2] == " "):
            return 2
    else:
        return -1

def checkForPossibleWin(board, char):
    if (checkForPossibleWinLine(board[0], char) != -1):
        return checkForPossibleWinLine(board[0], char) + 1
    elif(checkForPossibleWinLine(board[1], char) != -1):
        return checkForPossibleWinLine(board[1], char) + 4
    elif(checkForPossibleWinLine(board[2], char) != -1):
        return checkForPossibleWinLine(board[2], char) + 7
    elif(checkForPossibleWinLine([board[0][0], board[1][0], board[2][0]], char) != -1):
        return checkForPossibleWinLine([board[0][0], board[1][0], board[2][0]], char) * 3 + 1
    elif(checkForPossibleWinLine([board[0][1], board[1][1], board[2][1]], char) != -1):
        return checkForPossibleWinLine([board[0][1], board[1][1], board[2][1]], char) * 3 + 2
    elif(checkForPossibleWinLine([board[0][2], board[1][2], board[2][2]], char) != -1):
        return checkForPossibleWinLine([board[0][2], board[1][2], board[2][2]], char) * 3 + 2
    elif(checkForPossibleWinLine([board[0][0], board[1][1], board[2][2]], char) != -1):
        return checkForPossibleWinLine([board[0][0], board[1][1], board[2][2]], char) * 4 + 1
    elif(checkForPossibleWinLine([board[0][2], board[1][1], board[2][0]], char) != -1):
        return checkForPossibleWinLine([board[2][0], board[1][1], board[0][2]], char) * 2 + 3
    else:
        return -1

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

def getCellByNum(board, num):
    num -= 1
    return board[int(num / 3)][num % 3]

def setCellByNum(board, num, side):
    num -= 1
    board[int(num / 3)][num % 3] = side

def userTurn(board):
    num = int(input("Where would you like to move? "))
    setCellByNum(board, num, "X")
    displayBoard(board)

def placeCorner(board, place):
    if (place == 0):
        board[0][0] = "O"
    elif(place == 1):
        board[0][2] = "O"
    elif(place == 2):
        board[2][2] = "O"
    elif(place == 3):
        board[2][0] = "O"

def getNumBetweenCorners(a, b):
    if (a + b == 1):        # 0 - 1
        return 2;
    elif(a + b == 3 and abs(a - b) == 1):       # 1 - 2
        return 6;
    elif(a + b == 5 and abs(a - b) == 1):       # 2 - 3
        return 8;
    elif(abs(a - b) == 3):    # 3 - 0
        return 4;
    elif(a + b == 4):
        return 5
    elif(a + b == 2):
        return 5

def cornerToRegNum(num):
    if(num == 0):
        return 1
    elif(num == 1):
        return 3
    elif(num == 2):
        return 9
    elif(num == 3):
        return 7
def goalIsTie(board, goal):
    if(goal == "tie"):
        n = checkForPossibleWin(board, "O")
        if (n != -1):
            setCellByNum(board, n, "O")
        else:
            n = checkForPossibleWin(board, "X")
            if (n != -1):
                setCellByNum(board, n, "O")
            else:
                rand = random.randint(0, 9) + 1
                while (getCellByNum(board, rand) != " "):
                    rand = random.randint(0, 9) + 1
                setCellByNum(board, rand, "O")
        return True
    else:
        return False

def aiTurn(board, move, prevList, goal):
    prev = prevList[len(prevList) - 1]
    if (move == 0):
        rand = random.randint(0,3)
        prev = rand;
        placeCorner(board, prev)
    elif(move == 1):
        if (board[1][1] == "X"):
            prev = int((prev + 2) % 4)
            placeCorner(board, prev)
        else:
            rand = 2 * random.randint(0, 1)
            old = prev
            prev = int((prev + 3 + rand) % 4)
            print(getNumBetweenCorners(cornerToRegNum(prev), old))
            if (getCellByNum(board, cornerToRegNum(prev)) == "X" or getCellByNum(board, getNumBetweenCorners(prev, old)) == "X"):
                prev = int((prev + 2) % 4)
            placeCorner(board, prev)
    elif(move == 2):
        if (goalIsTie(board, goal)):
            print ()
        elif (getCellByNum(board, getNumBetweenCorners(prevList[1], prevList[2])) != "X"):
            setCellByNum(board, getNumBetweenCorners(prevList[1], prevList[2]), "O")
        else:
            a = len(prevList) - 2
            b = prev
            if (a == 0):
                a += 4
            if (b == 0):
                b += 4
            small = min(a, b)
            large = max(a, b)
            if (getCellByNum(board, cornerToRegNum(int((large + 1) % 4))) == "X" or getCellByNum(board, getNumBetweenCorners(int((large + 1) % 4), large)) == "X"):
                prev = int((small + 3) % 4)
                print("a")
            elif(getCellByNum(board, cornerToRegNum(int((small + 3) % 4))) == "X" or getCellByNum(board, getNumBetweenCorners(int((small + 3) % 4), small)) == "X"):
                prev = int((large + 1) % 4)
                print("b")
            else:
                rand = random.randint(0, 1);
                prev = int((large + 1 + rand) % 4)
                print("c")
            print(prev)
            placeCorner(board, prev)
    elif(move == 3):
        if (goalIsTie(board, goal)):
            print ()
        elif (getCellByNum(board, getNumBetweenCorners(prevList[3], prevList[1])) == " "):
            prev = getNumBetweenCorners(prevList[3], prevList[1])
        elif(getCellByNum(board, getNumBetweenCorners(prevList[3], prevList[2])) == " "):
            prev = getNumBetweenCorners(prevList[3], prevList[2])
        setCellByNum(board, prev, "O")
    else:
        for i in range(9):
            if (getCellByNum(board, i + 1)):
                prev = i + 1
        setCellByNum(board, prev, "O")
    displayBoard(board)
    return prev

def gamePlay(board):
    goal = "win"
    move = 0
    prev = [-1]
    prev.append(aiTurn(board, move, prev, goal))
    while(checkBoard(board) == "continue game"):
        move += 1
        userTurn(board);
        if (move == 1 and board[1][1] == "X"):
            goal = "tie"
        prev.append(aiTurn(board, move, prev, goal))
    print(checkBoard(board))

board = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]
gamePlay(board)
