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

    strng = strng.strip() # strip witespace, otherwise i return every whitespace
    while strng.find("  ") != -1: # look for double whitespaces
        strng = strng.replace("  "," ")# replace double ws with single ws
        
    words = [] # create list for result
    if strng == "": # look for empty string and return empty list 
        return words
    start = 0  # start of very first word
    while True: # infinite look, will stop when we don't find any whitespace any more
        wspace = strng.find(" ",start)
        if wspace == -1: # no wspace any more means we reached the final word
            word = strng[start:] # final word in string
            words.append(word)
            return words
        word = strng[start:wspace] # word between start and whitespace
        words.append(word) # add word to list
        start = wspace+1 # start of next word
    
    return words

print(mysplit("012 456 890"))
print(mysplit("Hi"))
print(mysplit("Hello my    friend"))
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
