
print("hi")   
print("hi")  


class A:
    def __init__(self,v=2):
        self.v=v
    def set (self,v=1):
        self.v += v
        return self.v
      
print("hi")      
a = A()
b=a
b.set()
print(a.v)
