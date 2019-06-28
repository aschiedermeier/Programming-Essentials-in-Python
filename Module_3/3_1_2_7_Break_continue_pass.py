#######################################
# 3.1.2.7 Loop control in Python
# break - continue - pass

# break - example
three = 0
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        three += 1
        break
    print("Inside the loop.", i)
print("Outside the loop.")
print ("Threes: " + str(three))

# continue - example
three = 0
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        three += 1
        continue
    print("Inside the loop.", i)
print("Outside the loop.")
print ("Threes: " + str(three))

# pass - example
three = 0
print("\nThe pass instruction:")
for i in range(1, 6):
    if i == 3:
        three = three +1
        pass
    print("Inside the loop.", i)
print("Outside the loop.")
print ("Threes: " + str(three))
