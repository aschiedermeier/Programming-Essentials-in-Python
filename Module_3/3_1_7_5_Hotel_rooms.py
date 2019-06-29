# 3.1.7.5 Lists in advanced applications | Arrays
# 3 dimensional matix
# hotel rooms
# 3 buildings
# 15 floors
# 20 rooms
# rooms full or occupied (True/False)

# list in list in list
rooms = [[[False for r in range(20)]for f in range(15)]for b in range(3)]
print (rooms)

# book room in the second building, on the tenth floor, room 14:
# rooms [bld][floor][room]
rooms [1][9][13] = True
# print (rooms)

# bld 1, flr 1, room 2
rooms [0][0][1] = True
# print (rooms)

# bld 3, flr 15, room 20
#rooms [2][14][19] = True
# print (rooms)

# same result (3,15,20)
if rooms [2][14][19] == True:
    print ("already booked")
else:
    rooms [2][14][19] = True
    print ("let me make a reservation")

# same result (3,15,20)
if rooms [-1][-1][-1] == True:
    print ("already booked")
else:
    rooms [-1][-1][-1] = True

# Check if there are any vacancies on the 15th floor of the third building:
vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1

print ("Vacancy on the 15th floor of the third building: ", vacancy) 