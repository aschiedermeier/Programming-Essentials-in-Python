# 6.1.3.1 OOP: Properties
# Instance variables

# 1. constructor unconditionally creates an instance variable named first.
# 2. method which creates another instance variable, named second.
# 3. exampleObject3 has been enriched with a property named third just on the fly, 
# outside the class's code - this is possible and fully permissible.


class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def setSecond(self, val):
        self.second = val


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.third = 5

print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)
print(exampleObject1.first)

###
# 6.1.3.2 OOP: Properties
# Instance variables: continued
# private instance variable

class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val	# instance variable becomes private due to two underscores

    def setSecond(self, val = 2):
        self.__second = val	# instance variable becomes private due to two underscores


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.__third = 5


print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)
print(exampleObject1._ExampleClass__first)	# __first becomes _ExampleClass__first