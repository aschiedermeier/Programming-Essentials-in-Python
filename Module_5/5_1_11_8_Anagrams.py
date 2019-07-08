# LAB
# 5.1.11.8 LAB: Anagrams

# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.

# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent

text1 = input("Word 1 pls: ")
text2 = input("Word 2 pls: ")

text1 = text1.lower()
text1= text1.replace(" ","")
text1 = list(text1)
text1.sort()

text2 = text2.lower()
text2= text2.replace(" ","")
text2 = list(text2)
text2.sort()

print (text1 == text2)
