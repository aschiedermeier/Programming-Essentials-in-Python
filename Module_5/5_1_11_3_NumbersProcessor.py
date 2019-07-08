# 5.1.11.3 Four simple programs

# The processing will be extremely easy 
# - we want the numbers to be summed.

# Numbers Processor

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")
