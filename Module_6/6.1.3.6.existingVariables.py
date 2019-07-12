# 6.1.3.6 OOP: Properties
# Checking an attribute's existence
# in Python you may not expect that all objects of the same class have the same sets of properties.

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1) # this object only has one attribute: a

print(exampleObject.a)
# print(exampleObject.b) #AttributeError: 'ExampleClass' object has no attribute 'b'


# 6.1.3.7 OOP: Properties
# Checking an attribute's existence: continued
# The try-except instruction gives you the chance to avoid issues with non-existent properties.


class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)
print(exampleObject.a)

try:
    print(exampleObject.b)
except AttributeError:
    pass

# hasattr function
# Python provides a function which is able to safely check if any object/class contains a specified property. 
# The function is named hasattr, and expects two arguments to be passed to it:
# the class or the object being checked;
# the name of the property whose existence has to be reported (note: it has to be a string containing the attribute name, not the name alone)

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)
print(exampleObject.a)

if hasattr(exampleObject, 'b'):
    print(exampleObject.b)

# 6.1.3.8 OOP: Properties
# hasattr() function can operate on classes, too.

class ExampleClass:
    attr = 1

print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))

# hasattr() function can operate on classes, too.

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2

exampleObject = ExampleClass()

print(hasattr(exampleObject, 'b')) #True: b is in object as variable
print(hasattr(exampleObject, 'a')) #True: a is in object in dictionary
print(exampleObject.a) # 1
print(exampleObject.b) # 2
print(exampleObject.a, exampleObject.__dict__) # a is herited class variable, in dictionary only b 
print(hasattr(ExampleClass, 'b')) #False
print(hasattr(ExampleClass, 'a')) #True
print(ExampleClass.__dict__) # has only a

