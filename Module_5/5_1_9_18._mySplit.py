# LAB
# 5.1.9.18 Your own split
# write your own function, which behaves almost exactly like the original split()
# it should accept exactly one argument - a string;
# it should return a list of words created from the string, divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;
# its name should be mysplit()


# debug:
# how to include last word: if sp != -1: just add last word
# what to do with several spaces

def mysplit(strng):

    words = []
    strng = strng.strip() # strip witespace, otherwise i return every whitespace
    start = 0
    if strng == "":
        return words
    while True:
        wspace = strng.find(" ",start)
        # print (wspace)
        if wspace == -1:
            word = strng[start:]
            words.append(word)
            return words
        word = strng[start:wspace]
        # print (word)
        words.append(word) 
        start = wspace+1
    
    return words

        
    """
    sp = strng.find(" ") # find first whitespace
    if sp == -1 and strng != "":
        words.append(strng) 
    wordstart = 0
    while sp != -1:
        word = strng[wordstart:sp] 
        wordstart = sp+1
        words.append(word) 
        sp = strng.find(" ", wordstart)

    return words
    """    
print(mysplit("012 456 890"))


print(mysplit("Hi"))
print(mysplit("Hello my    friend"))
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
