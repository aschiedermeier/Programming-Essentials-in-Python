print('''
6.1.5.12 OOP Fundamentals: Inheritance
Multiple inheritance occurs when a class has more than one superclass.
''')

class SuperA:
    varA = 10
    def funA(self):
        return 11

class SuperB:
    varB = 20
    def funB(self):
        return 21

class Sub(SuperA, SuperB): # two superclasses
    pass

obj = Sub()

print(obj.varA, obj.funA()) # class var and object var A
print(obj.varB, obj.funB()) # class var and object var B

print('''
6.1.5.13 OOP Fundamentals: Inheritance
''')

class Level1:
    var = 100 # this var has no influence on Level3
    def fun(self):# this fun has no influence on Level3
        return 101 

class Level2:
    var = 200
    def fun(self):
        return 201

class Level3(Level2):
    pass

obj = Level3() # obj inherits everything from Level 2

print(obj.var, obj.fun()) # 200 201

print('''
6.1.5.14 OOP Fundamentals: Inheritance
How does it work when a class has two ancestors offering the same entity, and they lie on the same level? 
''')

class Left:
    var = "L"
    varLeft = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    varRight = "RR"
    def fun(self):
        return "Right"

class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.varLeft, obj.varRight, obj.fun()) # L LL RR Left, as object takes properties from superclass 'Left'
