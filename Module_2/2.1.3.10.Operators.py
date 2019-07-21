# 2.1.3.10 Operators
# floor division
# modulo operator
# The exponentiation operator uses right-sided binding

# floor division
print(4 // 3)
print(4 // 3.)
print(4. // 3)
print(4. // 3.)

print()
# same result
print(-4 // 3," ",-4/3)
print(4 // -3," ",4/-3)

print()
print(3//4," ",3/4)
print(-3 // 4," ",-3/4)
print(3 // -4," ",3/-4)

# modulo
def mymodulo(a,b):
    print(a/b)
    print(a//b)
    print((a//b)*b)
    print(a-(a//b)*b)
    print(a%b)
mymodulo(12,4.5)

# different results
print()
print(4%2)
print(4%-2)
print(-4%2)
print(-4%-2)
print()
print(2%4)
print(2%-4)
print(-2%4)
print(-2%-4)

# right sided binding
print((1 ** 2 ** 3))
print((3 ** 2 ** 1))

# same priority and left side binding
print(2 * 3 % 5)

# compound assignment operators
a = 6
b = 3
a /= 2 * b
print(a)

# same result
a = 6
b = 3
a = a/ (2 * b)
print(a)
