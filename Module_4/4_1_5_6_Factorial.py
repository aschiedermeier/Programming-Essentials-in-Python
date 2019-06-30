# 4.1.5.6 Creating functions | factorials
# factorials
# 4! = 1 * 2 * 3 * 4
#It's marked with an exclamation mark, and is equal to the product of all natural numbers from one up to its argument.

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6): # testing
    print(n, factorialFun(n))

