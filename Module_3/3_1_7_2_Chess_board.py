# 3.1.7.2 Lists in advanced applications | Arrays
# Lists in lists: two-dimensional arrays
# chess board
# matrix 
# 3 ways to create a matrix

# need empty list to append to
# need to define variable
EMPTY = 0
board=[]
for i in range (8):
    row = [EMPTY for j in range(8)]
    board.append(row)
print (board)

# list gets created and filled
# need to define variable
FULL = 1
board1 = [[FULL for i in range(8)] for j in range(8)]
print (board1)

board2 = [[2 for i in range(8)] for j in range(8)]
print(board2)