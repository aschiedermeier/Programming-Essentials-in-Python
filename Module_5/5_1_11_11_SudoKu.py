# 5.1.11.11 LAB: Sudoku
# LAB
# reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
# each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
# each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
# each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

# function to check, if 1-9 is in a 9-digit string
def numsInString (strng):
    '''1-9 in string '''
    nums = "123456789"
    isin = True # is every digit in string? default yes, unless proven wrong
    for num in nums:
        pos = strng.find(num) # find digit in string in position pos
        if pos == -1: # if digit not in string, proven wrong, break loop
            isin = False
            return isin
    return isin

### ok
sdk=[
"295743861",
"431865927",
"876192543",
"387459216",
"612387495",
"549216738",
"763524189",
"928671354",
"154938672"]


# ### not ok
# sdk=[
# "195743862",
# "431865927",
# "876192543",
# "387459216",
# "612387495",
# "549216738",
# "763524189",
# "928671354",
# "254938671"]

isok = True


# check rows
for num in sdk:     # checks each element in list, representing the rows
    if numsInString(num) == False:
        isok = False
        break   # breaks for loop, no need to check the other rows    
print (isok)


# check columns
for i in range (9): # loop through all 9 columns
    col = ""    # empty string for columns
    for num in sdk:# loop though all 9 rows
        col = col + num[i]  # concatenate only the ith value in each row  
    if numsInString(col) == False:  
        isok = False    
        break       # breaks upper for i loop, no need to check other columns
print (isok)

# check squares

for i in range (0,7,3): # i = 0,3,6: defining the ranges for the squares
    for j in range  (0,7,3): # j = 0,3,6: defining the ranges for the squares 
        if isok == False:
            break   # need break command here, to stop checking other squares
        squ ="" # empty string for squares
        for a in range(0+i,3+i): # 3 to bottom
            for b in range (0+j,3+j): # 3 to right
                squ += sdk[a][b] # concatenate values from square
        if numsInString(squ) == False:
            isok = False
print (isok)
