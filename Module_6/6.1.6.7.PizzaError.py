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
        PizzaError.__init__(self, pizza, message)
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

# the error itself does not need to do much by itself.
# it can have args that can be called during the handling, e.g. variables or a message
class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uknown', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

# here i check for Errors using "if" and raise one if found
def makePizza(pizza, cheese):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError(pizza, "no such pizza on the menu")
	if cheese > 100:
		raise TooMuchCheeseError(pizza, cheese, "too much cheese")
	print("Pizza ready!")

# here i handle the Errors and handle them using "try except"
for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		makePizza(pz, ch)
	except TooMuchCheeseError as tmce:
		print(tmce, ':', tmce.cheese)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)