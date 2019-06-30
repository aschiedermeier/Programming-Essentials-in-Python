# 4.1.5.3 Creating functions | three-parameter function
# We know from school that the sum of two arbitrary sides has to be longer than the third side.
# In the second step, we'll try to ensure that a certain triangle is a right-angle triangle.
# We can also evaluate a triangle's field. Heron's formula will be handy here:

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(isItRightTriangle(5, 3, 4))
print(isItRightTriangle(1, 3, 4))

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def fieldOfTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return None
    return heron(a, b, c)

print(fieldOfTriangle(1., 1., 2. ** .5)) # 2. ** .5: squareroot of 2