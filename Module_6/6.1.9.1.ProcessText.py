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
Processing text files: continued

''')

from os import strerror as strerr # 'as strerr' was forgotten in original code

try:
    cnt = 0
    s = open('Module_6/text.txt', "rt")
    ch = s.read(1) # try to read the first character
    while ch != '': 
        print(ch, end='') # print character
        cnt += 1    # counter one up
        ch = s.read(1) # read() automatically skips one place, no need to add counter
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
    