# Part 1 summary test
# 45 mins
# 30 questions
# 70% passing score (21 correct)


print ("#1: runtime error")
# TypeError: cannot use * operator on "Nonetype"
def func1(a):
    return None
def func2(a):
    return func1 (a) * func1(a)
# here error
#print (func2(2))

print ("\n#02: [0,1,4,9]")
# careful: first look for value in list, then use value for position to delete
list = [x * x for x in range (5)]
#print (list) # lst=[0,1,4,9,16]
def fun(lst):
    del lst[lst[2]] # lst[2]=4, lst[4]=16
    return lst
    
print(fun(list))

print ("\n#03: AttributeError: 'dict' object has no attribute 'vals'")
# values() is the correct method
"""
dd = {"1":"0","0":"1"}
for x in dd.vals():
    print (x,end="")
"""
# correct code
dd = {"1":"0","0":"1"}
for x in dd.values():
    print (x,end="")   


print ("\n4: !=")
# operator to check whether two values not equal

print ("\n05: is erroneous - SyntaxError: non-keyworf arg after keyord arg")
def func (a,b):
    return b ** a
# here error    
# print (func(b=2,2))

print("\n#6: 4")
def fun(inp=2,out=3):
    return inp * out
print (fun(out=2))


print ("\n#7: fun(b=1)")
# ans: 
# TypeError: fun() missing 1 required positional argument: 'a'
def fun(a,b,c=0):
    print("hi")

fun (a=1,b=0,c=0)
fun (a=1,b=0)
fun (0,1,2)
# fun(b=1) # TypeError

print ("#18: 'in' is an illegal variable name")
# "in" is keyword
In = 1
in_ = 2
IN = 3
# in = 4

print ("#13:[1,1,1,2]")
# careful: update twice, so the position of lst[v] might change
# careful: to insert on final spot[-1] actually squeezes in to take spot[-2], instead of append on final spot
lst = [1,2]
for v in range(2):
    lst.insert(-1,lst[v])
print (lst)

print ("#17: 63")
#(enter 3 and 6)
y = "3"#input("3 pls")
x = "6"#input("6 pls")
print (x+y)

print ("#9: three #")
# checks list in list for uneven numbers
# every uneven numer (3 x 1) prints a #

lst = [[x for x in range(3)] for y in range(3)]
print (lst)
for r in range (3):
    for c in range (3):
        if lst [r][c] %2 != 0:
            print ("#")

print ("#5: nums and vals are different names of the same list")
nums = [1,2,3]
vals = nums

print ("#13: 21 or 12, is random!!!")

dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)

# print (dct)
# print (dct.keys())
# print (dct['1'])
for x in dct.keys():
    print(dct[x][1],end="")
    
print ("#14: 1//2 = 0")
# // returns rounded down to integer result of division
print (1//2)

print ("#23: nums and vals are different names of the same list")
nums= [1,2,3]
vals=nums#same lists; to get 2 seperate lists: vals=nums[:]
del vals[:]#deletes all values of both lists
print (vals)#returns empty list
print (nums)#returns empty list

print ("#26: x value: True")
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

print ("#19: 2")
def fun(x):
    if x%2 ==0:
        return 1
    else:
        return 2
print (fun(fun(2)))
# fun(2)= 1
# fun(1)= 2

print ("#25:2.0")
# x ** (1/2) is squareroot of x
x = float(2)#float(input("2 pls")) # input 2
y = float(4)#float(input("4 pls")) # input 4
print(y**(1/x))

print ("#22: 0")
x = int(3)#int(input("3 pls")) # enter 3
y = int(2)#int(input("2 pls")) # enter 2
x = x % y # 3 % 2 = 1
x = x % y # 1 % 2 = 1
y = y % x # 2 % 1 = 0
print(y)

print ("#15: 0 1")
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

print ("#2: 0")
def fun(x,y):
    if x ==y:
        return x
    else:
        return fun(x,y-1)
print (fun(0,3))

print("#11: one")
dct = {'one':'two', 'three':'one','two':'three'}
v = dct ['three'] # calling the value of the key 'one'--> 'two'

for k in range(len(dct)): # loop works, even without k in block
    v = dct[v] # v is not a number, but a key value. seems we are iterating though the key values
    # but the function variable v takes v from the outside, but does not give its value to the outside
    # threrefor this loop is just for confusion, v stays "one" from above
    
print (v)

print ("#11: zero")
# can't go backwards like this, use negative step
lst = [i for i in range(-1,-2)]
print (len(lst))

print ("#29: 1,1,2")
x = 1
y = 2
x,y,z = x,x,y # = 1,1,2
z,y,z = x,y,z # = 1,1,2 z becomes 1 first (from x) and then 2 (from z) again
print (x,y,z)

print ("#21: positional argument is determined by it's position within the argument list")

print("#1: is illegal, as tuples are immutable")
tuple1 =(1,2,3)
# causes error, as tuple object does not support item assignment
# tuple1[0] = tuple1[1] + tuple1[0]
print (tuple1)

# tuples can concatenate
tuple1 = tuple1 + tuple1
print (tuple1)

# it works with lists
list1 =[1,2,3]
list1[1] = list1[1] + list1[0]
print (list1)

print ("#27: 4")
tup = (1,2,4,8)
tup = tup [-2:-1] # tuple: (4,)
print (tup)
print (type(tup))
tup = tup [-1] # integer: 4
print (tup)
print (type(tup))

print ("#12: infinity loop")

"""
i= 0
while i < i +2:
    i +=1
    print ("*")
else:
    print("*")
"""

print ("#18: 0.2")
# floor division //: rounded down divison result
x = 1 // 5 + 1/5
print (x)

print ("#10: asepbsepc")
print ("a","b","c",sep="sep")
