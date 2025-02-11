#The purpose of this program is to determine as to whether the DTG provided by the User is valid or not.

validDate=True
minYear=0
minMonth=1
maxMonth=12
minDay=1
maxDay=31

year=int(input("Enter the year (0001-9999): "))
month=int(input("Enter the month (1-12): "))
day=int(input("Enter the day (1-31): "))
outputStatement=str(year) + str(month) + str(day)

if int(year) <= minYear:
    validDate=False
elif int(month) < minMonth or int(month) > maxMonth:
    validDate=False
elif int(day) < minDay or int(day) > maxDay:
    validDate=False
if validDate == True:
    print((outputStatement) + ("is a valid date"))
else:
    print((outputStatement) + ("is an invalid date"))