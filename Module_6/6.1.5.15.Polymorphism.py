print('''
6.1.5.15 OOP Fundamentals: Inheritance
Polymorphism 
How to build a hierarchy of classes
''')

class One:
    def doit(self):
        print("doit from One")

    def doanything(self):
        self.doit()

class Two(One):
    def doit(self): # overwrites doit method
        print("doit from Two") 

one = One()
two = Two()

one.doanything() # from One
two.doanything() # from Two

print('''
6.1.5.16 OOP Fundamentals: Inheritance
Polymorphism 
How to build a hierarchy of classes
''')

import time

class TrackedVehicle:
    def controltrack(left, stop):
        pass

    def turn(left): # problem: turn method defined twice, clumsy code
        controltrack(left, True)
        time.sleep(0.25)
        controltrack(left, False)


class WheeledVehicle:
    def turnfrontwheels(left, on):
        pass

    def turn(left): # problem: turn method defined twice, clumsy code
        turnfrontwheels(left, True)
        time.sleep(0.25)
        turnfrontwheel(left, False)
        

print('''
6.1.5.17 OOP Fundamentals: Inheritance
Polymorphism 
How to build a hierarchy of classes
''')

import time

class Vehicle: # superclass over both vehicle classes
    def changedirection(left, on): # abstract method for general scheme of turning, both subclasses will inherit but overwrite
        pass

    def turn(left): 
        changedirection(left, True)
        time.sleep(0.25)
        changedirection(left, False)

class TrackedVehicle(Vehicle):
    def controltrack(left, stop):
        pass

    def changedirection(left, on):
        controltrack(left, on)

class WheeledVehicle(Vehicle):
    def turnfrontwheels(left, on):
        pass

    def changedirection(left, on):
        turnfrontwheels(left, on)
        
print('''
6.1.5.18 OOP Fundamentals: Inheritance
Polymorphism 
How to build a hierarchy of classes
''')
import time

class Tracks:
    def changedirection(self, left, on):
        print("tracks: ", left, on)

class Wheels:
    def changedirection(self, left, on):
        print("wheels: ", left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.changedirection(left, True)
        time.sleep(0.25)
        self.controller.changedirection(left, False)

wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)