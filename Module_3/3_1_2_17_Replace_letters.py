
#Create a program with a for loop and a continue statement. 
# The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen. Use the skeleton below:

# use pass and == to not print 0
for digit in "0165031806510":
    if digit == "0":
        digit = "x" # line of code
        pass # line of code
    print (digit,end="") # line of code

# use print and continue, to not print 0
print()    
for digit in "0165031806510":
    if digit == "0":
        print ("x", end="") 
        continue # line of code
    print (digit,end="") # line of code