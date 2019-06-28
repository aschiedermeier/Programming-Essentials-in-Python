# 3.1.4.6 LAB: The basics of lists

hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hatList[2] = int(input("Number pls: "))

# Step 2: write a line of code here that removes the last element from the list.
del hatList[-1]

# Step 3: write a line of code here that prints the length of the existing list.
print(len(hatList))
print(hatList)