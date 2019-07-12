# 6.1.4.5 OOP: Methods
# The inner life of classes and objects
# atrributes

# __dict__

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()

print(obj.__dict__) # var:2
print(Classy.__dict__) # varia:1

# 6.1.4.6 OOP: Method
# __name__
print()

class Classy:
    pass

print(Classy.__name__) # Classy
obj = Classy()
# print(obj.__name__) # AttributeError
print(type(obj).__name__) # Classy

# 6.1.4.7 OOP: Method
# __module__
print()

class Classy:
    pass
# As you know, any module named __main__ is actually not a module, but the file currently being run.
print(Classy.__module__) # __main__
obj = Classy()
print(obj.__module__) # __main__
