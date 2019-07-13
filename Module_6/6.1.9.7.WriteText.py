print('''
6.1.9.7 Working with real files
write()
The method is named write() and it expects just one argument 
- a string that will be transferred to an open file
the open mode should reflect the way in which the data is transferred 
- writing a file opened in read mode won't succeed).
''')

from os import strerror as strerr

try:
	fo = open('newtext.txt', 'wt') # a new file (newtext.txt) is created
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))

print('''
6.1.9.8 Working with real files
write()
write whole lines to the text file.
''')


from os import strerror as strerr

try:
	fo = open('newlinetext.txt', 'wt')
	for i in range(10):
		fo.write("line #" + str(i+1) + "\n")
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))