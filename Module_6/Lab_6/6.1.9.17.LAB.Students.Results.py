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

from os import strerror

# enter filename 
# srcname = input("Hello Prof. Jekyll's, please enter file name: ")
# srcname = "stud.txt" # helper to skip file name


from os import strerror
try:
    ccnt = lcnt = 0
    s = open(srcname, "rt")
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
    print("I/O error occurred:", strerror(e.errno))




"""
text.txt 
John	Smith	5
Anna	Boleyn	4.5
John	Smith	2
Anna	Boleyn	11
Andrew	Cox	1.5"
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


for i in sorted(stud):
    print(i[0],i[1],stud[i])
    
    