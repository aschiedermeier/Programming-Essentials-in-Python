# 3.1.6.8 Lists - Find in List
# 1. Find location
# 2. Lottery 

# 1. Find location in list
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 5
found = False

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

# 2. Lottery
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

if hits:
    print("You have ", hits, " hits!")
else:
    print("Sorry, no hits.")