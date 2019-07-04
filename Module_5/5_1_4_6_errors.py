# 5.1.4.6 Errors - the programmer
# try except

################
# try except catches:
# b = 0
# a/b are not numbers
# can't see which one occured

print ("a/b pls:")
a = input("a pls ")
b = input("b pls ")
try:
    print(int(a)/int(b))
except:
    print("Can't do that")


#########
# the print("2") instruction was lost in the process.

try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")

#######
# catch 3 cases of exceptions

try:
    x = int(input("1/a -  Gimme 'a' pls: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")