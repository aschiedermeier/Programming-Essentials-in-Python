# 6.1.5.1 OOP Fundamentals: Inheritance
# default __str__() method / string method

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

sun = Star("Sun", "Milky Way")
# print like this does not look good, as it invokes the default __str__() method
print(sun) # "<__main__.Star object at 0x7f1074cc7c50>" object identifier

###
# defining new __str__() method
print()

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy

sun = Star("Sun", "Milky Way")
print(sun) # returns: "Sun in Milky Way"

# 6.1.5.4 OOP Fundamentals: Inheritance
# Inheritance: issubclass()
# check all possible ordered pairs of classes, 
# and to print the results of the check to determine 
# whether the pair matches the subclass-superclass relationship.
# each class is considered to be a subclass of itself.
print()

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()

##
# 6.1.5.5 OOP Fundamentals: Inheritance
# Inheritance: isinstance()
print()

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass


myVehicle = Vehicle()
myLandVehicle = LandVehicle()
myTrackedVehicle = TrackedVehicle()

for obj in [myVehicle, myLandVehicle, myTrackedVehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()


##
# 6.1.5.6 OOP Fundamentals: Inheritance
# Inheritance: the is operator

# The is operator checks whether two variables 
# (objectOne and objectTwo here) refer to the same object.

# Don't forget that variables don't store the objects themselves, 
# but only the handles pointing to the internal Python memory.
print() 

class SampleClass:
    def __init__(self, val):
        self.val = val

ob1 = SampleClass(0)
ob2 = SampleClass(2)
ob3 = ob1
ob3.val += 1

print(ob1 is ob2) #False
print(ob2 is ob3) #False
print(ob3 is ob1) #True
print(ob1.val, ob2.val, ob3.val) #1 2 1

str1 = "Mary had a little "
str2 = "Mary had a little lamb"
str1 += "lamb"

print(str1 == str2, str1 is str2) # True False
