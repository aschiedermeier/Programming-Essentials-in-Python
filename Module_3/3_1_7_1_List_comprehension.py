# 3.1.7.1 Lists in advanced applications
# list comprehension
# create list in one line
# list range if

# list  of pawns
WHITE_PAWN =[1]
row = [WHITE_PAWN for i in range(8)]
print (row)

# list of squares up to 9
squares = [x ** 2 for x in range(10)]
print(squares)

# list of powers to 2 up to 7 
twos = [2 ** i for i in range(8)]
print (twos)

# list of odds upt to 10
odds = [x for x in range(11) if x%2 !=0 ]
print (odds)

# list of odds from square list
oddsquares = [x for x in squares if x%2 !=0 ]
print (oddsquares)
