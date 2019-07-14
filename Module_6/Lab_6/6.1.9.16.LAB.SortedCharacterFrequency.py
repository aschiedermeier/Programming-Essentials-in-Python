print('''
6.1.9.16 LAB: Character frequency histogram
The output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
The histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' 
(it should be concatenated to the original name)
using lambda function and key parameter of sorted() function
''')


from os import strerror

srcname = input("Source file name?: ")
# srcname = "text.txt"


try:
    src = open(srcname, 'rt')
    content = src.read()
    content=content.lower()
    src.close()
#except Exception as exc:
#    print("The file could not be opened:", strerror(exc.errno))
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    exit() # stop program if load file error

# alphabet dictionary created using for loop for laziness reasons
# key: letter
# value: frequency, default 0
letters = {}
for char in range (97,123): # 122 is 'z'
    letters[chr(char)]=(0)

# addig letter count to dictionary, only lower case a-z - ignoring spaces, upper case and other characters
for ch in content:
    if ch in letters:   
        letters[ch]+=1   

# using key parameter and lambda function to reverse sort dictionary
# transformaiton into list
letters = sorted(letters.items(), key=lambda x: x[1],reverse=True)
# equivalent version
# sorted_d = sorted(d.items(), key=lambda (k,v): v,reverse=True)

# print result onscreen
print("Sorted Character Frequency Histogram:")
for x in letters:
    if x[1]!=0:
        line = str(x[0])+" ---> "+str(x[1]) # useful way for writing into file later
        print(line)

# name of outputfile
wrtname = srcname[0:-4]+".hist"

#write output into file
from os import strerror
try:
    fo = open(wrtname, 'wt') # a new file is created
    for x in letters:
        if x[1]!=0:
            line = str(x[0])+" ---> "+str(x[1])+"\n" # create line by line
            for ch in line: 
                fo.write(ch) # write char by char	
    fo.close()
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))

