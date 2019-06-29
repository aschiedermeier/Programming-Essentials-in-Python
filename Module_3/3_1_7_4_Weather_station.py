# 3.1.7.4 Lists in advanced applications | Arrays
# Lists in lists: two-dimensional arrays
# weather station
# temperature every hour: 24
# every day of the month: 31
# take average temp 

temps = [[0.0 for h in range(24)]for d in range(31)]
#print (temps)

# populate
temps [0][0]=20
temps [0][1]=22
temps [0][2]=23
temps [0][3]=25
temps [0][4]=26
temps [0][5]=27
temps [0][6]=24
print (temps)

# average temp at a given time
sum = 0.0
for day in temps:
    sum += day[5]
average = sum / 31

print("Average temperature at 6 a.m.:", average)

# highest temp all time
highest = -100.0
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

# count days where temp at 6 am was over 20
hotDays = 0
for day in temps:
    if day[5] > 20.0:
        hotDays += 1

print(hotDays, "mornings were hot.")