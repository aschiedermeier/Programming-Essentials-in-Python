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
	if mine: # if True
		raise MyZeroDivisionError("some worse news")
	else:	# if False		
		raise ZeroDivisionError("some bad news")

for mode in [False, True]:
	try:
		doTheDivision(mode)
	except ZeroDivisionError: # catches both errors, as it's the superError
		print('Division by zero')


for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('My division by zero') # catches only subError
	except ZeroDivisionError:
		print('Original division by zero') # catches subError and superError. Needs to be on the bottom
		
