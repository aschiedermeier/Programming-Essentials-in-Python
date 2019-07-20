#3.2.1.1
# Module test # 3



print("#1: != ")
# 1 ans: !=
# operator to check whether 2 values not equal


print("#2: 2")

i=2
while i >=0:
    print("*")
    i -=2

print("#3: 2")

for i in range (-1,1):
    print("#")


print("#4: True ")

z = 10
y = 0
x = z > y or z == y
print (x)



print("#5: [3,1,1]")
lst = [3,1,-1]
lst[-1]=lst[-2]
print (lst)


# 6: 
print("#6: does not change list's length")
vals = [0,1,2]
vals[0],vals[1]=vals[1],vals[2]
print(vals)


print("#7: nums and vals are of the smae length")
nums = []
vals = nums
vals.append(1)
print (nums)
print (vals)

# 8
print("#8: vals is longer than nums")
nums = []
vals = nums[:]
vals.append(1)
print (nums)
print (vals)

# 9 
print("#9: two")
l = [0 for i in range(1,3)]
print ([l])

# 10
print("#10: 0")
lst = [0,1,2,3]
x=1
for elem in lst:
    x*=elem
print (x)