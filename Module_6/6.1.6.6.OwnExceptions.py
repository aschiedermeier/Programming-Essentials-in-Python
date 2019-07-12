print('''
6.1.6.6 Exceptions once again
How to create your own exception
MyZeroDivisionError
It may be useful when you create a complex module which detects errors and raises exceptions, 
and you want the exceptions to be easily distinguishable from any others brought by Python.
This is done by defining your own, new exceptions as subclasses derived from predefined ones.
''')

class MyZeroDivisionError(ZeroDivisionError): # own exception derived from ZeroDivisionError
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("some worse news")
	else:		
		raise ZeroDivisionError("some bad news")

for mode in [False, True]:
	try:
		doTheDivision(mode)
	except ZeroDivisionError:
		print('Division by zero')


for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('My division by zero')
	except ZeroDivisionError:
		print('Original division by zero')
		
print('''
6.1.6.7 Exceptions once again
How to create your own exception: continued
PizzaError
When you're going to build a completely new universe filled with completely new creatures 
that have nothing in common with all the familiar things, 
you may want to build your own exception structure.
''')

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(message)
        self.pizza = pizza	


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese
        
print('''
6.1.6.8 Exceptions once again
How to create your own exception: continued
PizzaError

''')

class PizzaError(Exception):
    def __init__(self, pizza='uknown', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uknown', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def makePizza(pizza, cheese):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError
	if cheese > 100:
		raise TooMuchCheeseError
	print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		makePizza(pz, ch)
	except TooMuchCheeseError as tmce:
		print(tmce, ':', tmce.cheese)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)