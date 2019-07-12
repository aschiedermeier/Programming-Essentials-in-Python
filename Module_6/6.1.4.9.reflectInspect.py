# 6.1.4.9 OOP: Method
# Reflection and introspection
# The function named incIntsI() gets an object of any class, 
# scans its contents in order to find all integer attributes with names starting with i, 
# and increments them by one.

class MyClass:  # define class
    pass

obj = MyClass() # create object
obj.a = 1       # fill object with attributes
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys(): # look for attribute names
        if name.startswith('i'):    # if name starts with 'i'
            val = getattr(obj, name)    # get current value
            if isinstance(val, int):    # check if the value is of type integer, 
                setattr(obj, name, val + 1) # increment the property's value

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__) # var '1' and 'integer' been incresed by 1
