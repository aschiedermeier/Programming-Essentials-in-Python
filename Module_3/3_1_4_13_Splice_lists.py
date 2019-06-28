# splice lists
# delete certain items in the list

# del 2
a = [0,1,2,3,4,5]
del a[2]
print (a)

# 0,1
a = [0,1,2,3,4,5]
del a[:2]
print (a)

# 2,3,4,5
a = [0,1,2,3,4,5]
del a[2:]
print (a)

# 4
a = [0,1,2,3,4,5]
del a[-2]
print (a)

# 0,1,2,3
a = [0,1,2,3,4,5]
del a[:-2]
print (a)

# 4,5
a = [0,1,2,3,4,5]
del a[-2:]
print (a)