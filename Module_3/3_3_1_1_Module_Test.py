#3.3.1.1
# Module test # 3

# 1
print("#1: ")
lst= [i for i in range(-1,2)]
print (lst)

# 2
print("#2: ")
print (1==1)

# 3 
# error in test
# first print, as 0 is one value to be in range
# then jump into else, which also print one #
# total 2 # are printed
print("#3: ")
for i in range(1):
    print("#")
else:
    print("#")

# 4
print("#4: ")
var = 1 
while var < 10:
    print("#")
    var = var << 1

# 5
print("#5: ")
i = 0
while i <= 5:
    i +=1
    if i% 2 == 0:
        break
    print ("*")

# 6
print("#6: ")
var = 0
while var < 6:
    var+=1
    if var % 2 == 0:
        continue
    print("#")

# 7
# error in test, misread answer
# slacing backward only via negatice step
# therefore vals = []
print("#7: ")
nums = [1,2,3]
vals = nums [-1:-2]
print("nums: ", nums)
print("vals: ", vals)

# 8
print("#8: ")
lst1=[1,2,3]
lst2=[]
for v in lst1:
    lst2.insert(0,v)
print (lst2)

# 9 
print("#9: ")
i = 0
while i <= 3:
    i+=2
    print("*")

# 10
print("#10: ")
t= [[3-i for i in range(3)] for j in range (3)]
s = 0
for i in range(3):
    s+=t[i][i]
print (s)

# 11
print("#11: ")
lst =[1,2,3]
for v in range (len(lst)):
    lst.insert(1,lst[v])
print(lst)

# 12
print("#12: ")
nums = [1,2,3]
vals = nums
del vals[1:2]
print("nums: ", nums)
print("vals: ", vals)

# 13
print("#13: ")
lst = [[0,1,2,3,] for i in range(2)]
print ("runtime error if i run the  print line")
# # print (lst[2][0])

# 14
print("#14: ")
a = 1
b = 0
c = a & b
d = a |b
e = a^b
print(c+d+e)

# 15 
print("#15: ")
vals = [0,1,2]
vals.insert(0,1)
del vals[1]
print ("vals: ", vals)

# 16
print("#16: ")
vals = [0,1,2]
vals [0], vals[2]= vals [2], vals[0]
print(vals)

# 17
print("#17: ")
lst = [1,2,3,4]
print(lst[-3:-2])

# 18
# priority list: & --> | --> ^ 
print("#18: ")
z = 10
y = 0
x = y < z and z>y or y>z and z<y
print ("x: ", x)

# 19
print("#19: ")
x = 1
x = x == x
print ("x: ", x)

# 20
print("#20: ")
lst = [3,1,-2]
print(lst[lst[-1]])
