# 6.1.3.3 OOP: Properties
# Class variables

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)

print(exampleObject1.__dict__, exampleObject1.counter)
print(exampleObject2.__dict__, exampleObject2.counter)
print(exampleObject3.__dict__, exampleObject3.counter)



# 6.1.3.4 OOP: Properties
# 

class ExampleClass:
    __counter = 0	# mangling class variables name to make it private
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1

exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)

print(exampleObject1.__dict__, exampleObject1._ExampleClass__counter)
print(exampleObject2.__dict__, exampleObject2._ExampleClass__counter)
print(exampleObject3.__dict__, exampleObject3._ExampleClass__counter)
