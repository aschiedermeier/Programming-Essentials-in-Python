print('''
6.1.8.7 Processing files
File handles: continued
Opening the streams
The opening of the stream is performed by a function which can be invoked in the following way:

''')
# stream = open(file, mode = 'r', encoding = None)


print('''
6.1.8.9 Processing files
Opening the stream for the first time 
''')

try:
    stream = open("file.txt", "rt") 
    #stream = open("C:\Users\User\Desktop\file.txt", "rt")
    #stream = open("C:\Users\Andi\Desktop\file.txt", "rt")
    # in case of success we get an object from the open() function and we assign it to the stream variable;
    # processing goes here
    stream.close()
except Exception as exc:
    # if open() fails, we handle the exception printing full error information (it's definitely good to know what exactly happened)
    print("Cannot open the file:", exc) 
    