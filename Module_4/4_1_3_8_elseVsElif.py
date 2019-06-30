# while - if True - else vs while - if True - elif False


a = 0
while a < 10:
    if a%2 == 0:
        print ("Even ", a)
        a +=1
    else:
        print ("Odd ", a)
        a +=1

a = 0
while a < 10:
    if a%2 == 0:
        print ("Even ", a)
        a +=1
    elif a%2 == 1:
        print ("Odd ", a)
        a +=1