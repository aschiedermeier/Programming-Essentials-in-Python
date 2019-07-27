# Final Test
# 50 questions, 60 mins
# passing score 70%
# 78% at first try

print("""\n#1: 0
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

print("""\n#2: 1
    beware the extra brackets. It's a tuple with one integer inside. 
    The integer has no lenght, so len () returns error""")
print (len((1,)))
# print (len((1,)) # error

print("""\n#3: 1
    fun(1) = 1""")
def fun(x):
    return 1 if x %2 !=0 else 2
    
print(fun(fun(1)))

print("""\n#4: 0
    it's an empty list, as the range goes backwards.
    """)
print (len([i for i in range(0,-2)]))
# alternative for len = 2
print (len([i for i in range(0,-2,-1)]))

print("""\n#5: error: non-keyword after keyword argument""")
# def f(par2,par1):
#     return par2 + par1  
# print(f(par2=1,2))

# corrected code
def f(par2,par1):
    return par2 + par1
    
print(f(2,par1=1))

print("""\n#6: __init__.py is doing the intialize a package.
    It can be empty but must not be omitted.""")

print("""\n#7: *****
    x progress: 16 * 8 * 4 * 2 * 1* 0 end while loop""")
x = 16
while x > 0:
    print("*",end="")
    x//=2

print("""\n#8: finally branch always gets executed""")

print("""\n#9: 1 2 3
    the values get sorted""")

d = {"one":1,"three":3,"two":2}
for k in sorted(d.values()):
    print(k,end=" ")

# alternative code, sorts keys alphabetically
d = {"one":1,"two":2,"three":3}
for k in sorted(d.keys()):
    print(k,end=" ")

print("""\n#10:tuple
The BaseException class introduces a property named args. 
It's a tuple designed to gather all arguments passed to the class constructor. 
It is empty if the construct has been invoked without any arguments, or contains just one element when the constructor gets one argument (we don't count the self argument here), and so on.
 """)

print("""\n#11: ******
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
print("""\n#12: write()
    to write a byte array's content to a stream
    readinto() to read""")

print("""\n#13: error, as strings do not support item deletion.""")
# str = "abcdef"
# def fun(s):
#     del s[2]
#     return s

# print(fun(str))


print("""\n#14: 3.5""")
v = 1 + 1 // 2 + 1 /2 +2
print(v)

print("""\n#15: False True""")
class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass

x=X()
z=Z()
print(isinstance(x,Z),isinstance(z,X))

print("""\n#16: [2,4,6,8] in this case as correct answer
    misprint in lesson code, therefore error.""")
lt =[1,2,3,4]
lt=list(map(lambda x:2*x,lt))
print(lt)

print("""\n#17: 3
    first it becomes a one item tuple, then an integer""")
t = (1,2,3,4)
t=t[-2:-1]
t=t[-1]
print(t)

print("""\n#18: Keyword arguments are the ones whose meaning is not dictated by their location, but by a special word (keyword) used to identify them.
•	any keyword arguments have to be put after the last positional argument (this is very important)
""")

print("""\n#19: main""")
print(__name__)
print("""\n#20: stdout (as standard output) referring to the screen""")

print("""\n#21: """)

print("""\n#22: """)

print("""\n#23: """)

print("""\n#24: """)

print("""\n#25: """)

print("""\n#26: """)

print("""\n#27: """)

print("""\n#28: """)

print("""\n#29: """)

print("""\n#30: """)

print("""\n#31: """)

print("""\n#32: """)

print("""\n#33: """)

print("""\n#34: """)

print("""\n#35: """)

print("""\n#36: """)

print("""\n#37: """)

print("""\n#38: """)

print("""\n#39: """)

print("""\n#40: """)

print("""\n#41: """)

print("""\n#42: """)

print("""\n#43: """)

print("""\n#44: """)

print("""\n#45: """)

print("""\n#46: """)

print("""\n#47: """)

print("""\n#48: """)

print("""\n#49: """)

print("""\n#50: """)

