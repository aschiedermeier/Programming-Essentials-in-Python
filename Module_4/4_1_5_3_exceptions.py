# 5.1.5.3 The anatomy of exceptions
# several exceptions

# the order of the branches matters!
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

# don't put more general exceptions before more concrete ones;
try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
# This branch is now completely unreachable.
except ZeroDivisionError: 
    print("Zero Division!")

print("THE END.")

# handling two or more exceptions
try:
    y = 1 / 0
except (ArithmeticError,ZeroDivisionError):
    print("Arithmetic problem!")