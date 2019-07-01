# Module test # 4

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
# may not be used outside functions most probably false

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
# tuples are sequnce types.
# i think they can be indexed and sliced like lists.
# indexed for sure
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
v = dct ['one']
for k in range(len(dct)):
    v = dct[v]
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
# mistake: recheck
 
dct = {}
lst = ['a','b','c','d']
for i in range (len(lst)-1):
    dct[lst[i]] = (lst[i],)
for i in sorted(dct.keys()):
    k = dct[i]
    print(k)

# 15 
print("#15: ")
# mistake

# seems to be errorness, 
# as function object does not support deletion and item assignment
# list = ['Mary','had','a','little','lamb']
# def list(lst):
#     del lst[3]
#     lst[3]='ram'
# print(list(list))#

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
# come with Python, integral part of Python

# 20
print("#20: ")
# may be invoked without any argument, or jsut one
# mistake, i think

def function (x=0):
    return x

print (function())
print (function(0))
print (function(1))
