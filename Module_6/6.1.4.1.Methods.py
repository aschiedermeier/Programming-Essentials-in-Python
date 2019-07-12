# 6.1.4.1 OOP: Methods

class Classy:
    def method(self, par):
        print("method:", par)

obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

# 6.1.4.2 OOP: Methods

# The self parameter is used to obtain access to the object's instance and class variables.

class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var) # 2 3

obj = Classy()
obj.var = 3
obj.method()

# The self parameter is also used to invoke other object/class methods from inside the class.

class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

obj = Classy()  # class has no constructor, only methods. so nothing visible happens during instantiation
obj.method()    # calls method "method", which calls methods "other"
# output: method other
