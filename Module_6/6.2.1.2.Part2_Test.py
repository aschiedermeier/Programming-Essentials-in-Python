# 1
print("#1: error ")
#print (len("\\\"))

# 2
print("#2: invalid: object = Class(1,2) ")
class Class:
    def __init__(self,val=0):
        pass

# 3 
print("#3: AttributeError")
class A:
    def __init__(self,v):
        self.__a=v+1
        
a = A(0)
print(a.__a)



# 4
print("#4: False")
class A:
    pass
class B(A):
    pass
class C(B):
    pass

print(issubclass(A,C))

# 5
print("#5: False, as a is only in object, but not a class attribute")
class A:
    A=1
    def __init__(self):
        self.a = 0
        
print(hasattr(A,'a'))


# 6
print("#6: not more than one except block will be executed, if ther are more than one excetp")

print("#7: list containing all entities' names")
import math
print(dir(math))

# 8
print("#8: excepition, as class A takes no argument ")
class A:
    def __init__(self):
        pass
        
a = A(1)
print(hasattr(a,'A'))

# 9 
print("#9: 2")
print (len("\\\\"))


# 10
print("#10: 1.3 ")
print(float("1.3"))

# 11
print("#11: a")
try:
    raise Exception
except BaseException:
    print ("a")
except Exception:
    print("b")
except:
    print ("c")

# 12
print("#12: error, as 'var' is not defined ")
assert var !=0

# 13
print("#13: !! check it!!")
# file a.py
print ("a",end = "")

# file b.py
import a
print ("b",end = "")

# file c.py
print ("c",end="")
import a
import b

# 14
print("#14: !!! check home")
#for line in open('text.txt','rt'):

# 15 

print ("#15: pyc")


#compiled Python bytecode is stored in 

# 16
print("#16: b")
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

# 17
print("#17: check home - i  guess whole file")
for x in open('file','rt'):
    print(x)

# 18

print("#18: 3")
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
print("#19: readinto()")


# 20
print("#20: one character from the stream")
q = s.read(1)

# 21
print("#21: sys.stderr: the screen")


# 22
print("#22: __main__")
print(__name__)

# 23
print("#23: fun()")
from mod import fun

# 24
print("#24: ++++++")
def I(n):
    s = '+'
    for i in range (n):
        s += s
        yield s
    
for x in I(2):
    print(x,end="")

# 25 
print("#15: ***")
def o(p):
    def q():
        return '*' * p
    return q
    
r = o(1)
s = o(2)
print (r()+s())

# 26
print("#26: abc")
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
print("#27: 3")
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))

# 28
print("#28: error, as except must be last")
try:
    raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")

# 29
print("#29: r")
print (chr(ord('p')+2))

# 30
print("#30: entity c from module b from package a")

from a.b import c
