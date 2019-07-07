# LAB
# 5.1.9.18 Your own split
# write your own function, which behaves almost exactly like the original split()
# it should accept exactly one argument - a string;
# it should return a list of words created from the string, divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;
# its name should be mysplit()

def mysplit(strng):
#
# put your code here
#

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))