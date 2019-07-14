print('''
6.1.9.15 LAB: Character frequency histogram
ask the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
''')


from os import strerror

srcname = input("Source file name?: ")
try:
    src = open(srcname, 'rt')
    #src = open("text.txt", "rt")
    content = src.read()
    content=content.lower()
    src.close()
#except Exception as exc:
#    print("The file could not be opened:", strerror(exc.errno))
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    exit() # stop program if load file error


#content="aBcd, abc ab"
#content=content.lower()

print()
# created dictionary with alphabet using for loop for laziness reasons
# key: letter
# value: frequency, default 0
letters = {}
for char in range (97,123): # 122 is 'z'
    letters[chr(char)]=(0)


# counting the letters, only lower case a-z - ignoring spaces, upper case and signs
for ch in content:
    if ch in letters:   
        letters[ch]+=1   

# print out result, only non-zero values
print("Character Frequency Histogram:")
for key in sorted(letters.keys()):
    if letters[key]!=0:
        print(key, "-->", letters[key])
