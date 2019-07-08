# LAB
# 5.1.11.9 LAB: The Digit of Life

# Some say that the Digit of Life is a digit evaluated using somebody's birthday. 
# It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, 
# you have to repeat the addition until you get exactly one digit. For example:

# asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - 
# actually, the order of the digits doesn't matter)
# outputs the Digit of Life for the date.


date = input("Pls enter birthday in 8 digit format: ")

dol = 0
for i in range (8):
    dol += int(date[i])
 

if dol >= 11: 
    dol = dol//10 + dol%10
print(dol)
    
