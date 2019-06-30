#######################################
# 4.1.3.7 LAB: How many days: writing and using your own functions
# days in month
# function
# input: year, month
# return: days
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

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")