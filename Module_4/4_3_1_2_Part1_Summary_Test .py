# Module test # 4 - 2

# Module test # 4 - 2

# 1
print ("#1")
# ans: 4


# 2
# ans: 0

def fun(x,y):
    if x ==y:
        return x
    else:
        return fun(x,y-1)
        
print (fun(0,3))




#3
# ans: 21

dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)

# print (dct)
# print (dct.keys())
# print (dct['1'])
for x in dct.keys():
    print(dct[x][1],end="")


# 4

# ans: runtime error
# TypeError: cannot use * operator on "Nonetype"

def func1(a):
    return None

def func2(a):
    return func1 (a) * func1(a)

# here error
# print (func2(2))


# 5
# nums and vals are different names of the same list

nums = [1,2,3]
vals = nums


# 6
print ("#6")
# SyntaxError: non-keyworf arg after keyord arg
def func (a,b):
    return b ** a
# here error    
# print (func(b=2,2))


# 7
print ("#7")
# ans: one 

# 8
print ("#8")
# ans: fun(b=1)
# TypeError: fun() missing 1 required positional argument: 'a'

def fun(a,b,c=0):
    print("hi")

fun (a=1,b=0,c=0)
fun (a=1,b=0)
fun (0,1,2)
# fun(b=1)



# 9
print ("#9")
# ans: three
# checks this list in list for uneven numbers
# every uneven numer (3 x 1) prints a #

lst = [[x for x in range(3)] for y in range(3)]

print (lst)

for r in range (3):
    for c in range (3):
        if lst [r][c] %2 != 0:
            print ("#")



# 10
print ("#10")
# ans: asepbsepc


print ("a","b","c",sep="sep")


# 11
print ("#11")
# ans: zero
# can't go backwords like this, use negative step

lst = [i for i in range(-1,-2)]


# 12
print ("#12")
# ans: infinity loop

"""
i= 0
while i < i +2:
    i +=1
    print ("*")
else:
    print("*")
"""


# 13
print ("#13")
# ans:  [1,1,1,2]
# carful: update twice, so the positions switch around

lst = [1,2]

for v in range(2):
    lst.insert(-1,lst[v])
    
print (lst)

# 14
print ("#14")
# ans: 0
# // returns integer


print (1//2)



# 15
print ("#15")
# ans: 0 1
#a b xor
#0 0 0
#0 1 1 
#1 0 1
#1 1 0
a= 1
b= 0
a = a^b #= 1^0 =1
b = a^b #= 1^0 = 1
a = a^b #= 1^1 = 0 

print (a,b)


# 16
print ("#16")
# ans: illegal
# 
# causes error, as tuple object does not support item assignment

# 17
print ("#17")
# ans: 63

#(enter 3 and 6)
y = input("3 pls")
x = input("6 pls")
print (x+y)

# 18
print ("#18")
# ans: 0.2

x = 1 // 5 + 1/5
print (x)


# 19
print ("#19")
# ans: 2

def fun(x):
    if x%2 ==0:
        return 1
    else:
        return 2
        
print (fun(fun(2)))
# fun(2)= 1
# fun(1)= 2


# 20
print ("#20")
# ans: !=
# operator to check two values not equal


# 21
print ("#21")
# ans:  position within the argument list

# 22
print ("#22")
# ans: 0

x = int(input("3 pls")) # enter 3
y = int(input("2 pls")) # enter 2
x = x % y # 3 % 2 = 1
x = x % y # 1 % 2 = 1
y = y % x # 2 % 1 = 0
print(y)



# 23
print ("#23")
# ans: different names of the same list

nums= [1,2,3]
vals=nums
del vals[:]
print (vals)
print (nums)

# 24
print ("#24")
# ans: in = 4
# "in" is keyword


In = 1
in_ = 2
IN = 3
# in = 4

# 25
print ("#25")
# ans: 2.0
# x ** (1/2) is squareroot of x

x = float(input("2 pls")) # input 2
y = float(input("4 pls")) # input 4
print(y**(1/x))

# 26
print ("#26")
# ans: True

z = 0
y = 10
x = y < z and z > y or y > z and z < y

print(x)
x = 10 < 0 and 0 > 10 or 10 > 0 and 0 < 10
print(x)
x = False and False or True and True
print(x)
x = False or True
print(x)
x = True
print(x)


# 27
print ("#27")
# ans: 4


tup = (1,2,4,8)
tup = tup [-2:-1] # tuple: (4,)
print (tup)
print (type(tup))
tup = tup [-1] # integer 4
print (tup)
print (type(tup))

# 28
print ("#28")
# ans: [0,1,4,9]

list = [x * x for x in range (5)]
print (list)
def fun(lst):
    del lst[lst[2]] # lst[2]=4, lst[4]=16
    return lst
    
print(fun(list))


# 29
print ("#29")
# ans: #1,1,2


x = 1
y = 2
x,y,z = x,x,y # = 1,1,2
z,y,z = x,y,z # = 1,1,2

print (x,y,z)

# 30
print ("#30")
# ans: AttributeError: "dict" object has no attribute "vals"
# values() is the correct method
"""
dd = {"1":"0","0":"1"}
for x in dd.vals():
    print (x,end="")
"""
# correct code
dd = {"1":"0","0":"1"}
for x in dd.vals():
    print (x,end="")    
    


####################







# 1
print("#1: ")
# ans: illegal

tuple1 =(1,2,3)
# causes error, as tuple object does not support item assignment
# tuple1[0] = tuple1[1] + tuple1[0]
print (tuple1)

# it works with lists
list1 =[1,2,3]
list1[1] = list1[1] + list1[0]
print (list1)

# 2
print("#2: ")
# output 16

def func1(a):
    return a ** a
def func2(a):
    return func1(a) * func1(a)

print(func2(2))

# 3 
print("#3: ")
#ans: 6

def f(x):
    if x == 0:
        return 0
    return x + f(x-1)

print(f(3))


# 4
print("#4: ")
# ans: error

# function needs 2 arguments
def func(a,b):
    return a ** a
# gives error
# print(func(2))

# 5
print("#5: ")
# ans: 9
def fun(x,y,z):
    return x + 2 * y + 3 * z

print (fun(0, z=1,y=3))

# 6
print("#6: ")
# None value
# ans: may not be used outside functions (is false)

# None can be assigned to variables
# None can be compared with variables


# 7
print("#7: ")
# ans: def fun():

def fun():
    print ("Function")

fun()

# 8
print("#8: ")
# ans: 2

tup = (1,2,4,8)
tup = tup[1:-1]
tup = tup[0]
print (tup)

# 9 
print("#9: ")
# ans: they can be indexed and sliced like lists.
# tuples are sequnce types.
# can be deleted with del, but not modified

# 10
print("#10: ")
# runtime error

def fun(x):
    if x%2==0:
        return 1
    else:
        return

# error, as "None" cannot be used for addition
# print ( fun(fun(2)) +1)
# this one works
print ( fun(fun(2)+1))

# 11
print("#11: ")

# mistake: have to check!!!
# two

dct = {'one':'two', 'three':'one','two':'three'}
v = dct ['one'] # calling the value of the key 'one'--> 'two'
for k in range(len(dct)): # BS: k ist not in block
    v = dct[v] # BS: dict cannot be indexed, unless it's sorted
print (v)

# 12
print("#12: ")
# ans:4 

def fun(inp=2,out=3):
    return inp * out
print (fun(out=2))

# 13
print("#13: ")
# answer: 4
def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)

# 14
print("#14: ") 
# ans: print(k[0])
# mistake: supertricky one
 
dct = {}
lst = ['a','b','c','d']
for i in range (len(lst)-1):
    dct[lst[i]] = (lst[i],) #due to the comma it's a dictionary with tuples.
# without comma a dictionary with strings
for i in sorted(dct.keys()):
    k = dct[i]
    print(k[0])

###
# 14 in
dct = {}
dct1 = {}

lst = ['a','b','c','d']
for i in range (len(lst)-1):
    dct[lst[i]] = (lst[i],)
    dct1[lst[i]] = (lst[i])
    
print (sorted(dct))
print (type(dct))

print (sorted(dct1))
print (type(dct1))

for i in sorted(dct.keys()):
    k = dct[i]
    print (type(k))
    print(k)
    print(k[0])
    
for i in sorted(dct1.keys()):
    k = dct1[i]
    print (type(k))
    print(k)
    print(k[0])


# 15 
print("#15: ")
# mistake

# seems to be errorness, 
# as function object does not support deletion and item assignment
# list = ['Mary','had','a','little','lamb'] #cannot name a list "list"
# def list(lst):
#     del lst[3] # this actually affects the list outside the function
#     lst[3]='ram' # this too
# print(list(list)) # function does not return anything, so prints "None"
# print (liste) # this line here would print "print ['Mary','had','a','ram']

# working code
liste = ['Mary','had','a','little','lamb']
def list(lst):
    del lst[3]
    lst[3]='ram'
    print(lst)
print (liste)
print(list(liste))
print (liste)

# 16
print("#16: ")
# ans: 4

def fun(x):
    x+=1
    return x

x = 2
x = fun(x+1)
print(x)

# 17
print("#17: ")
# ans: 21

def any():
    print(var+1,end='')
var = 1
any()
print(var)

# 18
print("#18: ")

def fun(a=0, b=0):
    print (a+b)
fun()

# 19
print("#19: ")

# built-in function
# ans: come with Python, integral part of Python

# 20
print("#20: ")
# ans: may be invoked without any argument, or just one


def function (x=0):
    return x

print (function())
print (function(0))
print (function(1))
