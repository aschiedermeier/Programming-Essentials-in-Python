#######################################
# gregorian calendar
# function
# input: year
# return: year type
#######################################

def calendar(year):
    if year >= 1582:
        if (year%4) != 0:
            answer = "Common year"
        elif (year%100) != 0:
            answer = "Leap year"
        elif (year%400) != 0:
            answer = "Common year"
        else:
            answer = "Leap year"
    else:
        answer = "Not within the Gregorian calendar period"

    return answer