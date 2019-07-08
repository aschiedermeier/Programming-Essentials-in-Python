# LAB
# 5.1.11.7 LAB: Palindromes

# asks the user for some text;
# checks whether the entered text is a palindrome, and prints result.

# Do you know what a palindrome is?
# It's a word which look the same when read forward and backward. 
# For example, "kayak" is a palindrome, while "loyal" is not.

# assume that an empty string isn't a palindrome;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent;
# there are more than a few correct solutions - try to find more than one.

text = input("Enter your message: ")


text = text.lower()
text= text.replace(" ","")

rev = ""
for i in range(len(text)):
    rev += text [-1-i]

print (text == rev)
