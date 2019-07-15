print('''
6.1.9.17 LAB: Evaluating students' results
Your task is to write a program which:
asks the user for Prof. Jekyll's file name;
reads the file contents and counts the sum of the received points for each student;
prints a simple (but sorted) report, just like this one:
''')

#### missing
# read from file line by line
# https://edube.org/learn/programming-essentials-in-python-part-2/working-with-real-files-3
# https://github.com/aschiedermeier/Programming-Essentials-in-Python/blob/master/Module_6/6.1.9.1.ProcessText.py

# errors
"""
your program must be fully protected against all possible failures: 
the file's non-existence, the file's emptiness, 
or any input data failures; 
encountering any data error should cause immediate program termination, and the erroneous should be presented to the user;
implement and use your own exceptions hierarchy - we've presented it in the editor; 
the second exception should be raised when a bad line is detect, 
and the third when the source file exists but is empty.
"""
# todo:


from os import strerror

class StudentsDataException(Exception):
	pass

class BadLine(StudentsDataException):
	# put your code here
    pass

class FileEmpty(StudentsDataException):
	# put your code here
	pass
	
# enter filename 
# srcname = input("Hello Prof. Jekyll's, please enter file name: ")
srcname = "stud.txt" # helper to skip file name

# empty dictionary
stud ={}

# open and read file line by line
from os import strerror
try:
    ccnt = lcnt = 0
    s = open(srcname, "rt")
    line = s.readline() # read the first line
    while line != '':   # check if line is not empty
        print("line")
        print (line) #check
        b = line.split()
        print("line_split")
        print (b) #check 
        print("b_0")
        print(b[0])
        if (b[0],b[1]) in stud.keys():# if student in dict
            stud[(b[0],b[1])]+=float(b[2]) # add points
        else:   
            stud[(b[0],b[1])]=float(b[2]) # add student
        print("stud:",stud)
        line = s.readline() # check new line, if empty loop is broken
    s.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

print ("final result")
# present final result
for i in sorted(stud):
    print(i[0],i[1],stud[i])


"""
text.txt 
John	Smith	5
Anna	Boleyn	4.5
John	Smith	2
Anna	Boleyn	11
Andrew	Cox	1.5"
"""
"""

a = "John	Smith	5"
b = "Anna	Boleyn	4.5"
c = "John	Smith	2"
d = "Anna	Boleyn	11"
e = "Andrew	Cox	1.5"
text = [a,b,c,d,e]


stud ={}

for l in text:
    b = l.split()
    print (b)

    if (b[0],b[1]) in stud.keys():
        stud[(b[0],b[1])]+=float(b[2])
    else:
        stud[(b[0],b[1])]=float(b[2])

"""

"""
5.1.4.9.
# try except except block
# unnamed at the end
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except: 
    print("Oh dear, something went wrong...")

print("THE END.")
"""
    
    