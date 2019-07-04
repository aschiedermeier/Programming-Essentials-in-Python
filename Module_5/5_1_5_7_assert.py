# 5.1.5.7 The anatomy of exceptions | assert

import math

x = float(input("Squareroot x - Enter 'x' pls: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)