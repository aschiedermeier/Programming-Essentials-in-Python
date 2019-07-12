# 6.1.2.4 A short journey from procedural to object approach
# The stack - the object approach

class Stack:    # defining the Stack class
    def __init__(self):    # defining the constructor function
        print("Hi!")

stackObject = Stack()    # instantiating the object

# 6.1.2.5 A short journey from procedural to object approach
# The stack - the object approach: continued

class Stack:
    def __init__(self):
        self.stackList = []

stackObject = Stack()
print(len(stackObject.stackList))

# 6.1.2.6 A short journey from procedural to object approach
# encapsulation 
# AttributeError as __stacklist not accessible from outside the class

class Stack:
    def __init__(self):
        self.__stackList = []

stackObject = Stack()
print(len(stackObject.__stackList))