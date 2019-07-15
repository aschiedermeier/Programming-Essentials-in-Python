print('''
6.1.9.17 LAB: Evaluating students' results
Your task is to write a program which:
asks the user for Prof. Jekyll's file name;
reads the file contents and counts the sum of the received points for each student;
prints a simple (but sorted) report, just like this one:
''')

"""
your program must be fully protected against all possible failures: 
the file's non-existence, the file's emptiness, 
or any input data failures; 
encountering any data error should cause immediate program termination, and the erroneous should be presented to the user;
implement and use your own exceptions hierarchy - we've presented it in the editor; 
the second exception should be raised when a bad line is detect, 
and the third when the source file exists but is empty.
"""

from os import strerror

class StudentsDataException(Exception):
    def __init__(self,fileName,message):
        Exception.__init__(self,message)
        self.fileName=fileName

class BadLine(StudentsDataException):
    def __init__(self,fileName="",message="Bad data!"):
        StudentsDataException.__init__(self,fileName,message)
        self.fileName=fileName
    
class FileEmpty(StudentsDataException):
    def __init__(self,fileName="",message="Empty file:"):
        StudentsDataException.__init__(self,fileName,message)
        self.fileName=fileName

# enter filename 
srcname = input("Hello Prof. Jekyll's, please enter file name: ")
#srcname = "stud.txt" # helper to skip file name
#srcname = "stud_empty.txt" # helper for empty file Error
#srcname = "stud_bad_line.txt" # helper for bad line
#srcname = "stud1.txt" # helper for non existing text file - IOError

# empty dictionary
stud ={}

# open and read file line by line
from os import strerror
try:
    s = open(srcname, "rt") # open for reading text
    content = s.read()  # reading the whole file at once
    if content == "":   # check if empty
        raise FileEmpty(srcname) # raise Error with arg filename
    s.close()   # close file, so i can open again

    s = open(srcname, "rt") # open file again
    line = s.readline() # read the first line
    try:    # now check for Excepitions to raise BadLine Error
        while line != '':   # check if line is not empty
            b = line.split()    # split line into the 3 expected elements
            if (b[0],b[1]) in stud.keys():# if student in dict
                stud[(b[0],b[1])]+=float(b[2]) # add points
            else:   
                stud[(b[0],b[1])]=float(b[2]) # add student
            line = s.readline() # check new line, if empty loop is broken
    except Exception as e:  
            raise BadLine(srcname,message=e) # if somethings goes wrong raise BadLine Error
    s.close()   # close file when done
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    exit(e.errno)
except FileEmpty as fe: # catch FileEmpty Error
    print (fe, fe.fileName)
    exit()
except BadLine as bl: # catch BadLine Error
    print ("Bad data:",bl.fileName, bl,)
    exit()

print ("FINAL RESULT:")
# present final result
for i in sorted(stud):
    print(i[0],i[1],stud[i])
