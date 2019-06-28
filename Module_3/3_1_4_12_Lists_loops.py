# 3.1.4.12 Lists - collections of data | lists and loops
# Reverse order of list
# swap action

myList = [1,3,6,8,12,15,19]
print ("Start list: ", myList)
lenght = len(myList)

for i in range (lenght//2):
    myList[i],myList[lenght-1-i]=myList[lenght-1-i],myList[i]
print ("Reversed list: ", myList)