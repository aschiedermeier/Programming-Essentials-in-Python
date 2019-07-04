# 5.1.5.5 The anatomy of exceptions | raise


# raise inside of function
def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

#####
# raise without exception's name
# used inside the except branch only

def badFun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise

try:
    badFun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")