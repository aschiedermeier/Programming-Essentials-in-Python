# 3.1.2.17 SECTION SUMMARY
#Create a program with a for loop and a break statement. 
# The program should iterate over characters in an email address, 
# exit the loop when it reaches the @ symbol, and print the part before @ on one line. 
# Use the skeleton below:

# method 1: just print every char one after the other until the break
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

print()   
# method 2: save char and then print after the break
name =""
for ch in "max.doe@pythoninstitute.org":    
    if ch == "@":
        break
    name += ch

print (name)
