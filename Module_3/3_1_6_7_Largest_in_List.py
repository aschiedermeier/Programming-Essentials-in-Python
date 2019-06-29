# 3.1.6.7 Lists - largest in list

myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]

for i in myList:
    if i > largest:
        largest = i

print(largest)