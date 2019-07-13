print('''
6.1.9.1 Working with real files
Processing text files
if you're using a Unix/Linux OS configured to use UTF-8 as a system-wide setting, the open() function may look as follows:
''')
 

# vsc is looking for file in main folder (github), not in subfolder of py-life(module-6)
# cmd is looking for file in subfolder
# needed to make a copy of module_6-folder to open files from both locations
stream = open("Module_6/tzop.txt", "rt", encoding = "utf-8") # opening tzop.txt in read mode, returning it as a file object
print(stream.read()) # printing the content of the file

print('''
6.1.9.2 Working with real files
Reading a file character by character
''')

from os import strerror as strerr # 'as strerr' was forgotten in original code

try:
    cnt = 0
    #s = open('Module_6/text.txt', "rt")
    s = open('Module_6/huge.txt', "rt")
    ch = s.read(1) # try to read the first character
    while ch != '': 
        #print(ch, end='') # print character
        cnt += 1    # counter one up
        ch = s.read(1) # read() automatically skips one place, no need to add counter
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))

print('''
6.1.9.3 Working with real files
Reading a file as a whole
Remember - reading a terabyte-long file using this method may corrupt your OS.
A megabyte-long file took some time
''')

from os import strerror as strerr # 'as strerr' was forgotten in original code

try:
    cnt = 0
    s = open('Module_6/text.txt', "rt")
    content = s.read()  # reading the whole file at once
    for ch in content:
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))


print('''
6.1.9.4 Working with real files
readline()
The method tries to read a complete line of text from the file, 
and returns it as a string in the case of success. Otherwise, it returns an empty string.
''')


from os import strerror as strerr # 'as strerr' was forgotten in original code

try:
    ccnt = lcnt = 0
    s = open('Module_6/huge.txt', "rt")
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            # print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))

print('''
6.1.9.5 Working with real files
readlines()
The readlines() method, when invoked without arguments, 
tries to read all the file contents, and returns a list of strings, one element per file line.
''')

from os import strerror as strerr # 'as strerr' was forgotten in original code

try:
    ccnt = lcnt = 0
    s = open('Module_6/huge.txt', "rt")
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                #print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))


print('''
6.1.9.6 Working with real files
open()
A very interesting trait of the object returned by the open() function in text mode.
The object is an instance of the iterable class.
The iteration protocol defined for the file object is very simple 
- its __next__ method just returns the next line read in from the file.
The object automatically invokes close() when any of the file reads reaches the end of the file.
''')

from os import strerror as strerr # 'as strerr' was forgotten in original code

try:
	ccnt = lcnt = 0
	for line in open('Module_6/huge.txt', 'rt'):
		lcnt += 1
		for ch in line:
			#print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))