print('''
6.1.7.13 Generators and closures
A brief look at closures
closure is a technique which allows the storing of values in spite of the fact 
that the context in which they have been created does not exist anymore.

''')

def outer(par):
	loc = par
	def inner():
		return loc
	return inner

var = 1
fun = outer(var) # The function returned during the outer() invocation is a closure.
print(fun())

## closure example from final test
def a(x):
    def b():
        return x+x
    return b
    
x = a ('x')
y = a ('')
print(x()+y())

print('''
6.1.7.13 Generators and closures
A brief look at closures: continued
A closure has to be invoked in exactly the same way in which it has been declared.

''')

def makeclosure(par):
	loc = par
	def power(p):
		return p ** loc
	return power

fsqr = makeclosure(2)
fcub = makeclosure(3)
for i in range(5):
	print(i, fsqr(i), fcub(i))