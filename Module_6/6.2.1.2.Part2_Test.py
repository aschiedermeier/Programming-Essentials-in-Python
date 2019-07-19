# 1
print("\n#1: error - 2 or 4 escape characters are ok, but not 3")
#print (len("\\\"))

# 2
print("\n#2: invalid, as 3 positional arguments are given, only one or two accepted : object = Class(1,2)")
class Class:
    def __init__(self,val=0):
        pass
#object = Class(1,2)

# 3 
print("\n#3: AttributeError - as __ indicates private attribute, which needs to be called after mangling name: print(a._A__a)")
# class A:
#     def __init__(self,v):
#         self.__a=v+1
        
# a = A(0)
# print(a.__a)



# 4
print("\n#4: False, as A ist not subclass of C. print(issubclass(C,A)) is postive")
class A:
    pass
class B(A):
    pass
class C(B):
    pass

print(issubclass(A,C))

# 5
print("\n#5: False. A has only classattribute 'A', but not 'a'. 'a' is also a instance attribute")
class A:
    A=1 # a=1: then its True
    def __init__(self):
        self.a = 0
        
print(hasattr(A,'a'))

A = A() # onject called A
print(hasattr(A,'a')) # has attribute 'a'

# 6
print("\n#6: not more than one except block will be executed, if there are more than one except")

# 7
print("\n#7: list containing all entities' names")
import math
print(dir(math))

# 8
print("\n#8: exception, as class A takes no argument ")
# class A:
#     def __init__(self):
#         pass
        
# a = A(1)
# print(hasattr(a,'A'))

# 9 
print("\n#9: 2")
print (len("\\\\"))


# 10
print("\n#10: 1.3 ")
print(float("1.3"))

# 11
print("\n#11: a")
try:
    raise Exception
except BaseException:
    print ("a")
except Exception:
    print("b")
except:
    print ("c")

# 12
print("\n#12: will stop the program when var!= 0: answer is wrong, should be when var==0")
#assert var !=0

# 13
print("\n#13: cab")
# the initialization takes place only once, when the first import occurs, so the assignments done by the module aren't repeated unnecessarily.
# therefore 'a' gets printed only once
# file a.py
# print ("a",end = "")

# file b.py
# import a
# print ("b",end = "")

# file c.py
print ("c",end="")
import a
import b

# 14 #c
print("\n#14: is valid as open returns an iterable object")
for line in open('text.txt','rt'):
    print(line)

# 15 
print ("\n#15: compiled Python bytecode is stored in pyc")
#compiled Python bytecode is stored in 

# 16
print("\n#16: b, as double inheritance goes from left to right")
class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(B,A):
    def c(self):
        self.a()

o=C()
o.c()

# 17 # 
print("\n#17: line by line")
for x in open('file','rt'):
    print(x)

# 18
print("\n#18: 3 - be careful not to mix up v: variable & v: value. constuctor sets var = 2, b and a are connected, then method adds 1 on both")
class A:
    def __init__(self,v=2):
        self.v=v
    def set (self,v=1):
        self.v += v
        return self.v
       
a = A()
b=a
b.set()
print(a.v)

# 19
print("\n#19: readinto()")


# 20
print("\n#20: one character from the stream, i added extra lines of code to work")
#q = s.read(1)

s=  open('file','rt')
q = s.read(1)
print(q)

# 21
print("\n#21: sys.stderr: the screen")


# 22
print("\n#22: __main__, as it's opened in the program, not the module")
print(__name__)

# 23
print("\n#23: fun(), as we have mentioned fun() explicitly in the import line")
#from mod import fun

# 24
print("\n#24: 1+, but should be 6+ !!! ++++++")
def I(n):
    s = '+'
    for i in range (n):
        s += s
        yield s
    
for x in I(2):
    print(x,end="")

# 25 
print("\n#25: ***")
def o(p):
    def q():
        return '*' * p
    return q
    
r = o(1)
s = o(2)
print (r()+s())

# 26
print("\n#26: abc")
class I:
    def __init__(self):
        self.s = 'abc'
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v

for x in I():
    print(x,end='')


# 27
print("\n#27: 3")
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))

# 28
print("\n#28: error, as default 'except' must be last")
# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")

# 29
print("\n#29: r")
print (chr(ord('p')+2))

# 30
print("\n#30: entity c from module b from package a")

#from a.b import c
