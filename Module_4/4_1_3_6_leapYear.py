#######################################
# 4.1.3.6 LAB: A leap year: writing your own functions
# gregorian calendar
# function
# input: year
# return: LeapYear True/False
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


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")