print('''
6.1.7.9 Generators and closures
The lambda function
A lambda function is a function without a name (you can also call it an anonymous function). 
The declaration of the lambda function doesn't resemble a normal function declaration in any way - see for yourself:
lambda parameters : expression
Such a clause returns the value of the expression when taking into account the current value of the current lambda argument.
''')

two = lambda : 2
sqr = lambda x : x * x
pwr = lambda x, y : x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

print('''
6.1.7.10 Generators and closures
How to use lambdas and what for?
The most interesting part of using lambdas appears when you can use them in their pure form - 
as anonymous parts of code intended to evaluate a result.
Polynom function
''')

def printfunction(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

def poly(x):
	return 2 * x**2 - 4 * x + 2

printfunction([x for x in range(-2, 3)], poly)

print('''
Can we avoid defining the poly() function, as we're not going to use it more than once? 
Yes, we can - this is the benefit a lambda can bring.
''')

def printfunction(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

printfunction([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)


