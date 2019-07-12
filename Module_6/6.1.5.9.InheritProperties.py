print('''
# 6.1.5.9 OOP Fundamentals: Inheritance
# Inherit properties
# Class variables
''')

# Testing properties: class variables
class Super:
    supVar = 1 

class Sub(Super):
    subVar = 2

obj = Sub() # object has its own class variable variable and inherits the one from super 

print(obj.subVar) # 2
print(obj.supVar) # 1

print()
print('''
# Testing properties: overwriting class variables
''')
class Super:
    supVar = 1

class Sub(Super):
    supVar = 2 # in this case subclass overwrites inherited class variable

obj = Sub() # object has only one class variable with its own value

print(obj.supVar) # 2
print()

print('''
# 6.1.5.10 OOP Fundamentals: Inheritance
# Testing properties: instance variables
''')
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

obj = Sub()

print(obj.subVar) # 12 own instance var
print(obj.supVar) # 11 inherited instance var
print()

print('''
6.1.5.11 OOP Fundamentals: Inheritance
''')

class Level1:
    varia1 = 100
    def __init__(self):
        self.var1 = 101

    def fun1(self):
        return 102


class Level2(Level1):
    varia2 = 200
    def __init__(self):
        super().__init__()
        self.var2 = 201
    
    def fun2(self):
        return 202


class Level3(Level2):
    varia3 = 300
    def __init__(self):
        super().__init__()
        self.var3 = 301

    def fun3(self):
        return 302


obj = Level3()

print(obj.varia1, obj.var1, obj.fun1())
print(obj.varia2, obj.var2, obj.fun2())
print(obj.varia3, obj.var3, obj.fun3())