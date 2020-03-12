# Date: 03/12/2020 (lol ironic)
# Topic: Regular Expressions
#
# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range 
# from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.
# The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 
# 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect
# if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31
# days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, 
# unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular 
# expression that can detect a valid date.
# #######################################################################################################################################



import re ,sys

def date_validator(d,m,y):
    if month==2 and day in range(1,30):
        if  day==29  and (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
            print("Valid date with leap year")
    
    elif month in [4,6,9,11] and day in range(1,31):
        print("Date Exist in the Calander")
    elif month not in [4,6,9,11] and day in range(1,32) :
        print("Date Exist in the Calander")
    else:
        print("Non Existent Date")
    

# Starting Point
datecheck= input("Enter a date in this format dd/mm/yyyy:\t")

dateRegex = re.compile(r"^((\d{1,2}|0\d{1})/(\d{1,2}|0\d{1})/(\d{4}))$")  

try:
    mo=dateRegex.search(datecheck)
    # print(int(mo.group(2)))
    day=int(mo.group(2))
    month=int(mo.group(3))
    year= int(mo.group(4))
except:
    print("Somwthing went wrong....")
    sys.exit()

if day in range(0,32) and month in range(0,13) and year in range(1000,3000):
    date_validator(day,month,year)
else:
    print('''
Dates can have:
          Day: 1-31
          Month: 1-12
          Year: 1000-2999
    ''')
    

    

    

    
