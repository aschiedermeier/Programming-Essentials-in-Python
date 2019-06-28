#######################################
# gregorian calendar
# program to get year, run cal funct, return type
#######################################

from calendar_function import calendar

year = int(input("Enter a year: "))
answer = calendar(year)
print (answer)

# list of example values from the lesson
# quick and dirty alternative for unittesting
years = [2000,2015,1999,1996,1580]
for year in years:
    print (calendar(year))