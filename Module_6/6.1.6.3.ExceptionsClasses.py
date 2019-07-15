print('''
6.1.6.3 Exceptions once again
Exceptions are classes
when an exception is raised, an object of the class is instantiated, 
and goes through all levels of program execution, looking for the except branch that is prepared to deal with it.
''')

try:
    i = int("Hello!")
except Exception as e:
    print(e) # prints brief message about error
    print(e.__str__()) # identical effect
    
print()

try:
    i = 1/0
except Exception as e:
    print(e)
  

print()
try:
    raise Exception()
except Exception as e:
    print(e) # no message, as i only raised a generic message
   

print()
try:
    raise Exception("my Error Message")
except Exception as e:
    print(e) # message from argument 
  

