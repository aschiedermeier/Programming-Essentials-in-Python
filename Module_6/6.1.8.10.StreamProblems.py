print('''
6.1.8.10 Processing files
Diagnosing stream problems
The IOError object is equipped with a property named errno 
(the name comes from the phrase error number) and you can access it as follows:
''')

try:
    #s = open("c:/users/user/Desktop/file.txt", "rt")
    # s = open("C:\Users\Andi\Desktop\file.txt", "rt")
    s = open("file.txt", "rt")
    # C:\Users\Andi\Desktop\file.txt
    # some stream operations
except IOError as exc:
    print(exc.errno)
    print("errno!")

print('''
6.1.8.11 Processing files
Diagnosing stream problems
If you are a very careful programmer, 
you may feel the need to use the sequence of statements similar to those presented below:
''')

import errno
try:
    #s = open("c:/users/andi/Desktop/file.txt", "rt")
    s = open("file.txt", "rt")
    # actual processing goes here
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        printf("The error number is:", exc.errno)

print('''
6.1.8.11 Processing files
Diagnosing stream problems
Fortunately, there is a function that can dramatically simplify the error handling code. 
Its name is strerror(), and it comes from the os module and expects just one argument - an error number.
Its role is simple: you give an error number and get a string describing the meaning of the error.
''')

from os import strerror
try:
    # vsc is looking for file in main folder (github), not in subfolder of py-life(module-6)
    # cmd is looking for file in subfolder
    # needed to make a copy of module_6-folder to open files from both locations
    # in this case opening form vsc & cmd gives different results
    # s = open("c:/users/user/Desktop/file.txt", "rt")
    s = open("file.txt", "rt")
    # actual processing goes here
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))