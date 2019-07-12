# 6.1.4.8 OOP: Method
# attributes
# __bases__

class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


print (SuperOne.__bases__[0].__name__) # __bases__ is a tuple, so use index [0] to get class - then use __name__ for class name.
printBases(SuperOne) # a class without explicit superclasses points to object (a predefined Python class) as its direct ancestor.
printBases(SuperTwo) # a class without explicit superclasses points to object (a predefined Python class) as its direct ancestor.
printBases(Sub) # (SuperOne SuperTwo)
