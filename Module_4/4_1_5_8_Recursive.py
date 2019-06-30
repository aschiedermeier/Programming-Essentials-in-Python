
# Factorial
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

for n in range(1, 6): # testing
    print(n, factorialFun(n))


# Fibonacci
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(1, 10): # testing
    print(n, "->", fib(n))

# Recurvise
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))


