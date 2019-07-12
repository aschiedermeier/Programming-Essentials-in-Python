# 6.1.4.3 OOP: Methods
# constructor __init__

class Classy:
    def __init__(self, value): # constructor
        self.var = value

obj1 = Classy("object")

print(obj1.var) # output: object

# 6.1.4.4 OOP: Methods
# constructor __init__
print()

class Classy:
    def __init__(self, value = None): # a constructor with a default argument value
        self.var = value

obj1 = Classy("object")
obj2 = Classy()

print(obj1.var) # object
print(obj2.var) # None

# property name mangling
# 
print()

class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")

obj = Classy()
obj.visible() # visible method can be called with normal name: methodName()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden() # hidden method must be called with mangeled name: _className__methodName()
