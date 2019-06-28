# 3.1.2.11 LAB: The continue statement - the Pretty Vowel Eater
# exit while loops 
# continue statement
# check in list
# use concatenate to create string

wordWithoutVovels = ""
userWord = input("Word pls:").upper()

for letter in userWord:
    if letter in ["A","E","I","O","U"]:
        continue
    wordWithoutVovels = wordWithoutVovels + letter
print (wordWithoutVovels)
