# 5.1.9.4 String methods

# Demonstrating the find() method
print("Eta".find("ta"))
print("Eta".find("mma"))

# two-parameter variant of the find() method
print('kappa'.find('a')) # ans: 1
print('kappa'.find('a', 2)) # ans: 4

print()

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))