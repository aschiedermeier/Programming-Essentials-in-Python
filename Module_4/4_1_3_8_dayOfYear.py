#######################################
# 4.1.3.8 LAB: Day of the year: writing and using your own functions
# day of year
# function
# input: year, month, day
# return: weekday
#######################################

def isYearLeap(year):
    if year >= 1582:
        if (year%4) != 0:
            answer = False
        elif (year%100) != 0:
            answer = True
        elif (year%400) != 0:
            answer = False
        else:
            answer = True
    else:
        answer = "Not within the Gregorian calendar period"
    return answer

def daysInMonth(year, month):
    if isYearLeap(year) == True:
        monthLength = [31,29,31,30,31,30,31,31,30,31,30,31]
        return monthLength [month-1]
    else:    
        monthLength = [31,28,31,30,31,30,31,31,30,31,30,31]
        return monthLength [month-1]


def dayOfYear(year, month=1, day=1):
    # counter from first day of Gregorian Calendar
    # 1 is monday, 7 sunday
    runningDay = [5, 1582,1,1]
    # count until 1.1.of parameter year
    while runningDay [1] < year:
        if isYearLeap(runningDay [1]) == True:
            runningDay [0] += 2
            runningDay [1] += 1
        else:    
            runningDay [0] += 1
            runningDay [1] += 1


    # count until 1st of month in  parameter year
    if isYearLeap(runningDay [1]) == False:
        monthLength = [31,28,31,30,31,30,31,31,30,31,30,31]
    else:
        monthLength = [31,29,31,30,31,30,31,31,30,31,30,31]

    i = 0
    while runningDay[2] < month:
        runningDay [0] += monthLength[i]
        runningDay [2] += 1
        i += 1
    
    
    # for i in range(len(monthLength)):
    #     if  runningDay[2] == month:
    #         break
    #     else:
    #         runningDay [0] += monthLength[i]
    #         runningDay [2] += 1
    
        
    # count until parameter day
    while runningDay[3] < day:
        runningDay [0] += 1
        runningDay [3] += 1

    # transform daycount into ragne from 1 - 7
    runningDay [0] = runningDay [0]%7
    if runningDay [0] == 0:
        runningDay [0] = 7
    return runningDay [0]

# print (dayOfYear(1582,1,1))
# print (dayOfYear(1582,1,8))
# print (dayOfYear(1582,2,1))
# print (dayOfYear(1582,12,31))
# print()
# print (dayOfYear(1987,1,1))
# print (dayOfYear(1987,2,1))
# print (dayOfYear(1987,12,1))
# print (dayOfYear(1987,12,31))
# print()
# print (dayOfYear(1582,1))
# print (dayOfYear(1582,2))
# print (dayOfYear(1582,3))
# print (dayOfYear(1582,4))
# print()
# print (dayOfYear(1584,1))
# print (dayOfYear(1584,2))
# print (dayOfYear(1584,3))
# print (dayOfYear(1584,4))
# print()
# print (dayOfYear(1585))

# print (dayOfYear(1900))
# print (dayOfYear(1901))

# print (dayOfYear(2000))
# print (dayOfYear(2001))


testYears = [1900, 2000, 2019, 2019, 1987, 1582,1583,1975]
testMonths = [1, 1, 1, 6,12,1,1,6]
testDays = [1, 1, 1, 30,31,1,1,11]
testResults = [1, 6, 2,7,4,5,6,3]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	da = testDays[i]
	print(yr, mo, da, "->", end="")
	result = dayOfYear(yr, mo,da)
	if result == testResults[i]:
		print("OK: ", result)
	else:
		print("Failed: ",result)