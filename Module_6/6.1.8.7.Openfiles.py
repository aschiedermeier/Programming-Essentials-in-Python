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
    # processing goes here
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)