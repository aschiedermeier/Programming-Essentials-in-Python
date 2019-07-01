# 4.1.6.13 PROJECT: Tic-Tac-Toe
# tic tac toe game
# computer starts and plays random moves
# function playRound() keeps playing and keeps scoreboard

def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #
    print("+-------+-------+-------+")
    print("|",5*" ","|",5*" ","|",5*" ","|")
    print("|  ",board[0],"  |  ",board[1],"  |  ",board[2],"  |")
    print("|",5*" ","|",5*" ","|",5*" ","|")
    print("+-------+-------+-------+")
    print("|",5*" ","|",5*" ","|",5*" ","|")
    print("|  ",board[3],"  |  ",board[4],"  |  ",board[5],"  |")
    print("|",5*" ","|",5*" ","|",5*" ","|")
    print("+-------+-------+-------+")
    print("|",5*" ","|",5*" ","|",5*" ","|")
    print("|  ",board[6],"  |  ",board[7],"  |  ",board[8],"  |")
    print("|",5*" ","|",5*" ","|",5*" ","|")
    print("+-------+-------+-------+")

def EnterMove(board):
    #
    # the function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision
    #
    madeMove = False
    while madeMove == False:
        move = input("Your move: ")
        if move not in ["1","2","3","4","5","6","7","8","9"]:
            print ("Number from 1-9 pls!")
        elif board[int(move)-1] in  ["X","O"]:
            print ("Already taken!")
        else: 
            board[int(move)-1] = "O"
            madeMove = True
    DisplayBoard(board)
    return board
    

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#  
    free = []
    for i in range(9):
        if board[i]  not in   ("X","O"):
            free.append(board[i])
    #print (free)
    return free


def VictoryFor(game, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    won = False
    if sign == game[0] and sign == game[1] and sign == game[2]:
        won = True
    if sign == game[3] and sign == game[4] and sign == game[5]:
        won = True
    if sign == game[6] and sign == game[7] and sign == game[8]:
        won = True
    if sign == game[0] and sign == game[3] and sign == game[6]:
        won = True
    if sign == game[1] and sign == game[4] and sign == game[7]:
        won = True
    if sign == game[2] and sign == game[5] and sign == game[8]:
        won = True
    if sign == game[0] and sign == game[4] and sign == game[8]:
        won = True
    if sign == game[6] and sign == game[4] and sign == game[2]:
        won = True
    return won

def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    import random as rn
    freeOnes = MakeListOfFreeFields(board)
    spot = rn.randint(0,len(freeOnes)-1)
    board[freeOnes[spot]-1] = "X"
    print ("Computer picked ", freeOnes[spot])
    DisplayBoard(board)
    return board

    # # computer just fills the first free field
    # freeOnes = MakeListOfFreeFields(board)
    # board[freeOnes[0]-1] = "X"
    # print ("Computer moved")
    # DisplayBoard(board)
    # return board

def Play():
    #board = ["O","O","X","O","X",6,7,8,9]
    board = [1,2,3,4,"X",6,7,8,9]
    print ("Let's play!")
    DisplayBoard(board)
    while True:
        board = EnterMove(board)
        if VictoryFor(board, "O"):
            print ("Player won!")
            return "Player"
        if MakeListOfFreeFields(board) == []:
            print ("Draw")
            return 
        board = DrawMove(board)
        if VictoryFor(board, "X"):
            print ("Computer won!")
            return "Computer"
        if MakeListOfFreeFields(board) == []:
            print ("Draw")
            return    

def playRound():
    print ("Let's play a round of Tic Tac Toe!\nComputer plays X and places the first move.")
    print ("Player plays O")
    play = True
    playerWin = 0
    compWin = 0
    while play:
        ans = input("Wanna play? Type any key except 'n'\n")
        if ans != "n":
            winner = Play()
            if winner == "Player":
                playerWin += 1
            if winner == "Computer":
                compWin += 1
            print ("End of this game")
            print ("Player: ", playerWin, "\nComputer: ", compWin)
        else:
            print ("See you, thanks for playing")
            play = False

playRound ()
      