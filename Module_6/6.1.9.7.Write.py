print('''
6.1.9.7 Working with real files
write()

''')

from os import strerror

try:
	fo = open('newtext.txt', 'wt') # a new file (newtext.txt) is created
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))