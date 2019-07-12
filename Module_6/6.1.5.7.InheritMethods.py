# 6.1.5.7 OOP Fundamentals: Inheritance
# Inherit methods

class Super:
    def __init__(self, name): # class own constructor
        self.name = name    # constructor used to assign the property "name"

    def __str__(self):
        return "My name is " + self.name + "." # str method to present name in clear form

class Sub(Super):
    def __init__(self, name): # Subclass with own constructor
        Super.__init__(self, name) # invoking superclass constructor


obj = Sub("Andy") # object of Subclass

print(obj) # "My name is Andy", as subclass called __str__ method of superclass

print()

# 6.1.5.8 OOP Fundamentals: Inheritance
# Inherit methods
# super() function

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Super):
    def __init__(self, name):
        super().__init__(name) # super() function accesses the superclass without knowing the name


obj = Sub("Andy")

print(obj)