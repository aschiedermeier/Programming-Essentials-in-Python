# 3.1.7.3 Lists in advanced applications | Arrays
# Lists in lists: two-dimensional arrays
# Fill chess board
# matrix 

# create empty chess board
EMPTY = "-"
board = [[EMPTY for i in range(8)] for j in range(8)]
print (board)

# populate board
ROOK = "ROOK"
board [0][0] = ROOK
board [0][7] = ROOK
board [7][0] = ROOK
board [7][7] = ROOK
print (board)