# LAB
# 5.1.11.6 LAB: Improving the Caesar cipher

# The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. 
# Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.
# Moreover, let the code preserve the letters' case 
# (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.
# Caesar cipher

text = input("Enter your message: ")

coorectInput = False
while coorectInput == False:
    shift = int(input("Enter shift value from 1 to 25: "))
    if shift < 1:
        print ("Higher pls!")
    elif shift > 25:
        print ("Lower pls!")
    else:
        coorectInput = True

cipher = ''
for char in text:
    if ord('A') <= ord(char) <= ord('Z'):
        code = ord(char) + shift    
        if code > ord('Z'):
            code = code - 26
                
    elif ord('a') <= ord(char) <= ord('z'):
        code = ord(char) + shift    
        if code > ord('z'):
            code = code - 26   
            
    else:
        code = ord(char)
    cipher += chr(code)

print(cipher)