# Final Test
# 50 questions, 60 mins
# passing score 70%
# 78% at first try

for i in range (50):
    print ()
    
print("""\n#1: True
    and operator superior to or
    """)
y = 1
z = 2
x = y < z or z > y and y > z or z <y
print(x)
# extra code
x = y < z or (z > y and y > z) or z <y
print(x)

x = z > y and y > z
print(x)

x = (y < z or z > y) and (y > z or z <y)
print(x)

x = y < z or z > y 
print(x)

x =  y > z or z <y
print(x)

# or chain starting with True always stays True
x = True or False or False or False
print (x)

print("""\n#2: 2
    (1,) is a tuple
    t[0] is 1 is an integer""")
t = (1,)
t=t[0]+t[0]
print (t)

print("""\n#3: 1 2 3""")
x,y,z = 3,2,1
z,y,x=x,y,z
print(x,y,z)

print("""\n#4: True
    C is subbclass from both A and B""")
class A:
    pass
class B:
    pass
class C(A,B):
    pass
print (issubclass(C,A)and issubclass(C,B))

print("""\n#5: __init__.py may contain a file intended to intialize a package.
    It can be empty but must not be omitted.""")

print("""\n#6: error, as strings do not support item deletion.""")
try:
    str = "abcdef"
    def fun(s):
        del s[2]
        return s
    print(fun(str))
except Exception as e:
    print (e)

print("""\n#7: True
    class A hast the classattribute 'A' (has to be string)
    """)
class A:
    A=1
    def __init__(self):
        self.a=0
        
print(hasattr(A,'A'))

print("""\n#8: 1
    line break counts as one""")
x= """
"""
print(len(x))
# extra code
print(type(x))
print (x)

print("""\n#9: list
    The readlines() method, when invoked without arguments, 
    tries to read all the file contents, and returns a list of strings, one element per file line.
    """)

print("""\n#10: fun(a=1,b=0,c=0)
    provides the 2 positional arguments required""")
def fun(a,b,c=0):
    return

fun(a=1,b=0,c=0)

print("""\n#11: two
    list has 3 elements
    each a list of length: 0,1,2
    for loop prints empty line for first 2 lists
    """)
ls = [[c for c in range(r)]for r in range(3)]
for x in ls:
    if len(x)<2:
        print ()
        
# extra code
ls = [[c for c in range(r)]for r in range(3)]
print(ls)
for x in ls:
    print (x)
    print(len(x))
    if len(x)<2:
        print ("*")

print("""\n#12: 1
    ok like this, as there are  extra brackets. 
    It's a tuple with one integer inside. 
    With less brackets only integer ->  integer has no lenght, so len () returns error""")
print (len((1,)))
# extra code with one pair of brackets less
try:
    print (len(1,))
except Exception as e:
    print (e)

# compare types
print (type((1,)))
print (type(1,))
print (type(1))

print("""\n#13: 5
    class variable A - progress: 1,2,3
    instance variable a- 2,3,5""")
class A:
    A = 1
    def __init__(self,v=2):
        self.v = v+A.A
        A.A +=1
        
    def set(self,v):
        self.v +=v
        A.A +=1
        return
    
a = A()
a.set(2)
print(a.v)

print("""\n#14: object = Class()
    constructor takes only one argument (self), which does not need to be given explicitly.
    also "None" counts as one argument too much")
    """)
class Class:
    def __init__(self):
        pass  
object = Class()
print (object)
print (object.__str__())
print (object.__class__)

try:
    object = Class(None) # error, None is one argument too much.
except Exception as e:
    print (e)
    

print("""\n#15: XX
    b is a closure and returns 2 X's""")
def a(x):
    def b():
        return x+x
    return b
    
x = a ('x')
y = a ('')
print(x()+y())

## non closure version
def a(x):
    return x+x
    
print(a('x'))    
x = a ('x')
y = a ('')
print(x+y)

print("""\n#16: 1
    _a is a normal instance variable
    __a would be a private/hidden instance variable.""")
class A:
    def __init__(self,v):
        self._a=v+1       
a = A(0)
print(a._a)

# extra code: hidden/private variable
class A:
    def __init__(self,v):
        self.__a=v+1     
a = A(0)
try:
    print(a.__a) # error, as __a is hidden
except Exception as e:
    print (e)
print(a._A__a) # mangling to call hidden variable

print("""\n#17: 0
    empty list with len 0""")
print (len([i for i in range(0,-2)]))
# extra code
print([i for i in range(0,-2)])

print("""\n#18: ac
    BaseExceptiion is below Exception and catches it.
    else branch gets skipped, as except caught Exception
    finally branch always gets taken""")
try:
    raise Exception
except BaseException:
    print("a",end = "")
else:
    print("b",end="")
finally:
    print("c")

print("""\n#19: start its name with _ or __
    to tell your module users that a particular variable
    should not be accessed directly.""")

print("""\n#20: 21
    input is a string, therefore concatenation instead of addition""")
y = "1"#input()
x = "2"#input()
print(x+y)

print("""\n#21: *****
    x progress: 16 * 8 * 4 * 2 * 1 * 0, end while loop""")
x = 16
while x > 0:
    print("*",end="")
    x//=2

print("""\n#22: error
    SyntaxError: default 'except' must be last""")
# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")


print("""\n#23: ******
    n is 3, so 3 loops in for loop
    s progress: * , **, *** 
    x is not an integer, as it's the result from I(), which yields s --> only stars """)
def I(n):
    s=""
    for i in range(n):
        s+="*"
        yield s
        
for x in I(3):
    print(x,end="")

print("""\n#24: the screen
    sys.stdout stream (as standard output) referring to the screen""")

print("""\n#25: False True""")
class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass

x=X()
z=Z()
print(isinstance(x,Z),isinstance(z,X))

print("""\n#26: a string ending with a long hexadecimal number
    print(a.name) to get the name variable""")
class A:
    def __init__ (self,name):
        self.name=name
        
a = A("class")
print(a)
# extra code
print(a.name)

print("""\n#27:tuple
The BaseException class introduces a property named args. 
It's a tuple designed to gather all arguments passed to the class constructor. 
It is empty if the construct has been invoked without any arguments, or contains just one element when the constructor gets one argument (we don't count the self argument here), and so on.
 """)

print("""\n#28: 0
    d: dictionary, lenght 4
    for loop makes 4 loops
    each time x becomes d[x], so the key becomes the value
    4 times alternating between 0 & 1
    final value for x: 0""")
d = {1:0,2:1,3:2,0:1}
x=0
for y in range(len(d)):
    x=d[x]  
print (x)

print("""\n#29: __main__
    when you run a file directly, its __name__ variable is set to __main__;
    when a file is imported as a module, 
    its __name__ variable is set to the file's name (excluding .py)""")
print(__name__)

print("""\n#30: 1 2 3
    the values get sorted""")

d = {"one":1,"three":3,"two":2}
for k in sorted(d.values()):
    print(k,end=" ")

# alternative code, sorts keys alphabetically
d = {"one":1,"two":2,"three":3}
for k in sorted(d.keys()):
    print(k,end=" ")


print("""\n#31: a
    C inherits a from A and B. So it's from A, as it's most left""")
class A:
    def a(self):
        print("a")
        
class B:
    def a(self):
        print("b")
        
class C(A,B):
    def c(self):
        self.a()
        
o = C()
o.c()

print("""\n#32: [2,4,6,8] in this case as correct answer
    misprint in lesson code, therefore error.""")
lt =[1,2,3,4]
lt=list(map(lambda x:2*x,lt))
print(lt)

print("""\n#33: write()
    to write a byte array's content to a stream
    readinto() to read""")

print("""\n#34: one
    i progress: 4 ,2, print "*", equals 2, 
    break while loop, skip else branch, as while was chosen before""")

i = 4
while i > 0:
    i-=2
    print("*")
    if i == 2:
        break
else:
    print("*")

print("""\n#35: exception
    g needs (self) argument in definition
    Here, both functions have a parameter named self at the 
    first position of the parameters list.
    Is it needed? Yes, it is.
    All methods have to have this parameter. 
    It plays the same role as the first constructor parameter.
    """)
    
class A:
    def __init__(self):
        pass
    def f(self):
        return 1
    def g():
        return self.f()

try:
    a = A()
    print(a.g())
except Exception as e:
    print (e)

## corrected code
class A:
    def __init__(self):
        pass
    def f(self):
        return 1
    def g(self):
        return self.f()

a = A()
print(a.g())

print("""\n#36: a'b'c""")
print("a","b","c",sep="'")

print("""\n#37: None
    function does not return any value
    the execution in the fun is legitimate""")
def fun(d,k,v):
    d[k]=v
    
dc={}
print(fun(dc,'1','v'))

print("""\n#38: str1 and str2 are different (but equal) strings""")
str1='string'
str2=str1[:]

print("""\n#39: 3
    first it becomes a one item tuple, then an integer""")
t = (1,2,3,4)
t=t[-2:-1]
t=t[-1]
print(t)

print("""\n#40: True False""")
a = True
b = False
a = a or b
b = a and b
a = a or b
print (a,b)

print("""\n#41: 1
    fun(1) = 1""")
def fun(x):
    return 1 if x %2 !=0 else 2
    
print(fun(fun(1)))

print("""\n#42: 24
    in newer versions of pyhthon dict is ordered by addition (not alphabetically)
    older versions: outcome 42 or 24 by chance""")
d = {}
d['2']=[1,2]
d['1']=[3,4]
for x in d.keys():
    print(d[x][1],end="")

print("""\n#43: function cannot be invoked
    from f import m: import statement is invalid, as f is the function
    correct:from module import function""")

print("""\n#44: error: non-keyword after keyword argument""")
def f(par2,par1):
    return par2 + par1  
try:
    eval("print(f(par2=1,2))")
except Exception as e:
    print (e)

# corrected code    
print(f(2,par1=1))

print("""\n#45: 3.5""")
v = 1 + 1 // 2 + 1 /2 +2
print(v)

print("""\n#46: error
    The backslash (\) has a very special meaning when used inside strings - this is called the escape character.
    The word escape should be understood specifically - it means that the series of characters in the string escapes for the moment (a very short moment) to introduce a special inclusion.
    In other words, the backslash doesn't mean anything in itself, but is only a kind of announcement, that the next character after the backslash has a different meaning too.
""")
try:
    eval('x ="\"')
    print(len(x))
except Exception as e:
    print (e)

print("""\n#47: ==
    operator whether two variables are equal""")

print("""\n#48: the arguments name specified along with its value
    Keyword arguments are the ones whose meaning is not dictated by their location, 
    but by a special word (keyword) used to identify them.
    any keyword arguments have to be put after the last positional argument (this is very important)
""")

print("""\n#49: finally branch always gets executed""")

print("""\n#50: __pycache__
    the folder created by Pyhton where pyc files are stored""")


