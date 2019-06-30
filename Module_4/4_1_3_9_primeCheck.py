# 4.1.3.9 LAB: Prime numbers - how to find them

def isPrime(num):
    Prime = True
    i= 2
    while Prime is True:
        if i == num:
            break
        if num%i == 0:
            Prime = False
            break
        else:
            i+=1
    return Prime


request = int(input("Prime numbers until what number? Must be above 1! "))
counter = 0
for i in range (2,request+1):
    if isPrime(i):
        counter +=1
        highest = i
        print ("Prime #", counter,": ", i)

print ("Total amount prime numbers until ",request, " is: ", counter,"\nHighest one: ", highest)
