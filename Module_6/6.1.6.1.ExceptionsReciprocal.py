print('''
6.1.6.1 Exceptions once again
try except else block
''')

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:   # there can be more than one branch
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n

print(reciprocal(2))
print(reciprocal(0))

print('''
6.1.6.2 Exceptions once again
try except else finally block
''')

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:    # is always executed
        print("It's time to say goodbye")
        return n

print(reciprocal(2))
print(reciprocal(0))