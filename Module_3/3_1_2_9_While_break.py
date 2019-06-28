# 3.1.2.9 LAB: The break statement - Stuck in a loop
# exit while loops 
# usage of break possible but not necessary

word = ""
while word != "abc":
    word = input("Word pls:")
print ("You've successfully left the loop.")

while True :
    word = input("Word pls:")
    if word == "abc":
        break
print ("You've successfully left the loop.")
    
    

