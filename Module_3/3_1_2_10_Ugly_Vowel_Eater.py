# 3.1.2.10 LAB: The continue statement - the Ugly Vowel Eater
# exit while loops 
# continue statement
# check in list

userWord = input("Word pls:")
for letter in userWord.upper():
    if letter in ["A","E","I","O","U"]:
        continue
    print (letter)
