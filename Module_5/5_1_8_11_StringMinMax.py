# 5.1.8.11 The nature of strings in Python

# Demonstrating min() - Example 1
# Upper before Lower
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3
# space before letters
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')


t = [0, 1, 2]
print(min(t))

# Demonstrating max() - Example 1
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))