# 4.1.4.1 Scopes in Python


# A variable existing outside a function has a scope inside the functions' bodies.
print ("Scope Example # 1:")
def myFunction():
    print("Do I know that variable?", var)

var = 1 # scope from outside to inside function. 
# It's sufficient to assing this after funtion def.
# just before invoking function is enough.
myFunction()
print(var)

# A variable existing outside a function has a scope inside the functions' bodies, 
# excluding those of them which define a variable of the same name.
# It also means that the scope of a variable existing outside a function is supported 
# only when getting its value (reading). Assigning a value forces the creation of the function's own variable.

print("Scope Example # 2:")
def myFunction():
    var = 2 # scope only inside
    print("Do I know that variable?", var)

var = 1 # scope only outside, as var is defines inside function, too.
print(var)
myFunction()
print(var)

print("Scope Example # 3:")
# There's a special Python method which can extend a variable's scope 
# in a way which includes the functions' bodies (even if you want not only to read the values, 
# but also to modify them).
# Such an effect is caused by a keyword named global.

# Using this keyword inside a function with the name (or names separated with commas) of a variable(s), 
# forces Python to refrain from creating a new variable inside the function - 
# the one accessible from outside will be used instead.
# In other words, this name becomes global (it has a global scope, 
# and it doesn't matter whether it's the subject of read or assign).

def myFunction():
    global var 
    var = 2 # scope also outside, due to global
    print("Do I know that variable?", var)

var = 1
print(var) # var = 1, from outside
myFunction()
print(var) # var = 2, from inside function, due to global


print("Scope Example # 4:")
# if the argument is a list, then changing the value of the corresponding 
# parameter doesn't affect the list 
# (remember: variables containing lists are stored in a different way than scalars)
# but if you change a list identified by the parameter 
# (note: the list, not the parameter!), the list will reflect the change.

def myFunction(myList1):
    print(myList1)
    myList1 = [0, 1]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)

print("Scope Example # 5:")
def myFunction(myList1):
    print(myList1)
    del myList1[0]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)

