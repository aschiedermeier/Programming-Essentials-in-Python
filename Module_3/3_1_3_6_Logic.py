# Logic and bit operations in Python 
# Bitwise operators
# Bit shifting

x = 4
y = 1
print (bin(x))
print (bin(y))

a = x & y 
b = x | y
c = ~x # -x-1
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print("x == y: ", x == y)
print("(x == y) and (x == y): ", (x == y) and (x == y))
print("not(x == y): ", not(x == y))
print("False or True: ", False or True)
print("z: ",z)
print("not(z): ",not(z))