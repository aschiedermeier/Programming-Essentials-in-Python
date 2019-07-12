print('''
6.1.7.4 Generators and closures
The yield statement
yield turns the function into a generator, and executing the yield statement has some very interesting effects.
There is one important limitation: such a function should not be invoked explicitly 
as - in fact - it isn't a function anymore; it's a generator object.
The invocation will return the object's identifier, not the series we expect from the generator.
''')

def fun(n):
    for i in range(n):
        yield i
        
print(type(fun(5)))
print(fun(5))

for v in fun(5):
    print(v)
    
print('''
6.1.7.5 Generators and closures
How to build your own generator
a generator to produce the first n powers of 2?

''')

def powersOf2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *= 2
for v in powersOf2(8): # iterate range(8)
    print(v)
    
s = [x for x in powersOf2(5)] # list comprehension
print(s)
print(type(s))

t = list(powersOf2(5)) # The list() function can transform a series of subsequent generator invocations into a real list:
print(t)
print(type(t))

for i in range(20):
    if i in powersOf2(4):
        print(i)
        
print('''
Fibonacci number generator
''')
def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(Fib(10))

print(fibs)