# 5.1.6.4 Reading ints safely
# LAB

def readint(prompt, min, max):

    entered = False
    while entered == False:
        try:
            ans = int(input(prompt))
        except ValueError:
            print ("Error: wrong input")
            continue
        if  not (min <= ans <= max):
            print ("Error: the value is not within permitted range (min..max)")
        else: 
            entered == True
            return ans
            
            

v = readint("Enter a whole number from -10 to 10: ", -10, 10)

print("The number is:", v)