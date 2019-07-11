# 6.1.5.1 OOP Fundamentals: Inheritance
# default __str__() method / string method

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

sun = Star("Sun", "Milky Way")
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