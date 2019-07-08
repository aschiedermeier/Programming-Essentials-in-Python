# 5.1.11.10 LAB: Find a word!
# LAB

# Let's play a game. 
# We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.
# Your task is to write a program which answers the following question: 
# are the characters comprising the first string hidden inside the second string?

# sort string by transforming into list, sorting, then join back to string
# find function only works on strings
strng = "vcxzxduybfdsobywuefgas" # where we want to search in
print(strng)
strng = strng.lower()
strng = list(strng)
strng.sort()
strng = "".join(strng)

# transfer into list, so i can sort alphabetically
chars = "dog" # what we want to search for
print(chars)
chars = chars.lower()
chars = list(chars)
chars.sort()


isin = True # is every char in string? default yes, unless proven wrong
pos = 0 # startplace to look for. gets pushed plus one, each time we find new char to avoid double finds
for char in chars:
    pos = strng.find(char,pos) # is char in string, start looking a startplace pos
    if pos == -1: # if char not in string, proven wrong, break loop
        isin = False
        break
    pos += 1 # increase pos, to avoid double find
print (isin)


