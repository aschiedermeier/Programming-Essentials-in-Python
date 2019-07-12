print('''
6.1.7.1 Generators and closures
Generators - where to find them
A Python generator is a piece of specialized code able to produce a series of values, 
and to control the iteration process. This is why generators are very often called iterators, 
and although some may find a very subtle distinction between these two, we'll treat them as one.
''')

for i in range(5):
    print(i)
    
print('''
6.1.7.2 Generators and closures
Generators - where to find them
Fibonacci numbers
The iterator protocol is a way in which an object should behave to conform to the rules 
imposed by the context of the for and in statements. 
An object conforming to the iterator protocol is called an iterator.
''')
class Fib:
	def __init__(self, nn):
		print("__init__")
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		print("__iter__")		
		return self

	def __next__(self):
		print("__next__")				
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

for i in Fib(10):
	print(i)

print('''
6.1.7.3 Generators and closures
Generators - where to find them
Fibonacci numbers
This is why the output of the code is the same as previously, 
although the object of the Fib class isn't used explicitly inside the for loop's context.
''')

class Fib:
	def __init__(self, nn):
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		print("Fib iter")
		return self

	def __next__(self):
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

class Class:
	def __init__(self, n):
		self.__iter = Fib(n)

	def __iter__(self):
		print("Class iter")
		return self.__iter;

object = Class(8)

for i in object:
	print(i)