print('''
6.1.7.12 Generators and closures
Lambdas and the filter() function
It expects the same kind of arguments as map(), but does something different 
- it filters its second argument while being guided by directions flowing from the function 
specified as the first argument (the function is invoked for each list element, just like in map()).
''')

from random import seed, randint

seed()
data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)

## my own filter

filtered = list(filter(lambda x: x > 2,[x for x in range(5)]))
print(filtered)