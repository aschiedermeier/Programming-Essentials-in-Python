# 5.1.5.4 The anatomy of exceptions

# exception is raised inside a function
# handling inside the function

def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

badFun(0)

print("THE END.")

# exception is raised inside a function
# handling outside the function

def badFun(n):
    return 1 / n

try:
    badFun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")