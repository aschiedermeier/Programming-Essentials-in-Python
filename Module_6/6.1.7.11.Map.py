print('''
6.1.7.11 Generators and closures
Lambdas and the map() function
The map() function applies the function passed by its first argument to all its second argument's elements, 
and returns an iterator delivering all subsequent function results. 
You can use the resulting iterator in a loop, or convert it into a list using the list() function.

''')

list1 = [x for x in range(5)]

list2 = list(map(lambda x: 2 ** x, list1))
print(list2)

for x in map(lambda x: 2 ** x, list1):
	print(x, end=' ')
print()


print(list(map(lambda x: 2 ** x, [x for x in range(5)])))
