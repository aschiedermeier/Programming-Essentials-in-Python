print('''
6.1.9.9 Working with real files
6.1.9.10 Working with real files
Bytearray
a specialized class containing (amorphous) bytes.
''')


data = bytearray(10) # constructor creates a bytearray object able to store ten bytes and fills it with zeros

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))
    

print('''
6.1.9.11 Working with real files
Write bytearray
Read bytearray
''')

from os import strerror as strerr

data = bytearray(10)

for i in range(len(data)):
    data[i] = ord('a') + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))



from os import strerror as strerr

data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))

print('''
6.1.9.12 Working with real files
read()
Invoked without arguments, it tries to read all the contents of the file into the memory, 
making them a part of a newly created object of the bytes class.
This class has some similarities to bytearray, with the exception of one significant difference - it's immutable.
Don't use this kind of read if you're not sure that the file's contents will fit the available memory.
''')

from os import strerror as strerr

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file1.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))


# enter code that reads bytes from the stream here
from os import strerror as strerr

try:
    bf = open('file1.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerr(e.errno))

print('''
6.1.9.13 Working with real files
read()
If the read() method is invoked with an argument, it specifies the maximum number of bytes to be read.
''')

from os import strerror as strerr

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file2.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))



# enter code that reads bytes from the stream here
from os import strerror as strerr

try:
    bf = open('file2.bin', 'rb')
    data = bytearray(bf.read(5))
    # Note: the first five bytes of the file have been read by the code - the next five are still waiting to be processed.
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerr(e.errno))