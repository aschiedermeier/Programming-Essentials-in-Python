# 4.1.6.1 Tuples and dictionaries

tuple1 = (1, 2, 4, 8)
tuple2 = 1., .5, .25, .125

print(tuple1)
print(tuple2)

# create empty tuple
emptyTuple = ()

print(emptyTuple)

# one-element tuple
oneElementTuple1 = (1, )
oneElementTuple2 = 1., 
notATuple = 1

print (oneElementTuple1)
print (oneElementTuple2)
print (notATuple)

# +, * - operators, len () function, in, not in - operators work for tuples
myTuple = (1, 10, 100)

t1 = myTuple + (1000, 10000)
t2 = myTuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in myTuple)
print(-10 not in myTuple)

# One of the most useful tuple properties is their ability to appear on the left side of the assignment operator. 
# You saw this phenomenon some time ago, when it was necessary to find an elegant tool to swap two variables' values.
# a tuple's elements can be variables, not only literals. 

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)