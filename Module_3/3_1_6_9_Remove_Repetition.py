# 3.1.6.9 LAB: Operating with lists - basics
# Remove repeting elements in list
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

newList=[]

for i in myList:
    if i not in newList:
        newList.append(i)
    

print("The list with unique elements only:")
myList = newList[:]
print(myList)