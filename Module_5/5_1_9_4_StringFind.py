# 5.1.9.4 String methods

# Demonstrating the find() method
print("Eta".find("ta")) # ans: 1
print("Eta".find("mma")) # ans: -1

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

fnd = txt.find('the') # finds first one
while fnd != -1:      # as long as it's still found
    print(fnd)        # output location
    fnd = txt.find('the', fnd + 1) # make new search one step after last found one

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

# Demonstrating the rfind() method
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))