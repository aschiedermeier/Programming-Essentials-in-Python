# 5.1.8.3 The nature of strings in Python

########################
# concatenate
# replicate


str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# Demonstrating the ord() function

ch1 = 'a' 
ch2 = ' ' # space

# ans: 97
print(ord(ch1))
# ans: 32
print(ord(ch2))

# Demonstrating the chr() function

print(chr(97))
print(chr(945))

x="1"
print (chr(ord(x)) == x)
x=1
print (ord(chr(x)) == x)