# 5.1.9.5 String methods
# Isalnum method

# Demonstrating the isalnum() method
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum()) # empty string

t = 'Six lambdas' # space is not digit or letter
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

# Example 1: Demonstrating the isapha() method
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method
print('2018'.isdigit())
print("Year2019".isdigit())

# Example 1: Demonstrating the islower() method
print("Moooo".islower())
print('moooo'.islower())

# Example 2: Demonstrating the isspace() method
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example 3: Demonstrating the isupper() method
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())