# 6.1.3.5 OOP: Properties
# difference between these two __dict__ variables, 

class ExampleClass:
    varia = 1   # class variable
    def __init__(self, val): # constructor
        #ExampleClass.varia = val    # sets class variable with parameter's value. Output: 1,2,empty
        # self.varia = val # create an instance variable of the same name as the class's one. Output: 1,1,2
        varia = val # operate on a method's local variable. output: 1,1,empty
        
print(ExampleClass.__dict__) # var: 1
exampleObject = ExampleClass(2)

print(ExampleClass.__dict__) # var: 2
print(exampleObject.__dict__) # object's __dict__ is empty - the object has no instance variables.
