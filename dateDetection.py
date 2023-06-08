import re

dateDetectionRegex = re.compile(r'''(
    (\d{2})
    (/)
    (\d{2})
    (/)
    (\d{4})
    )''', re.VERBOSE)

mo = dateDetectionRegex.search('02/29/2016')

month = int(mo.group(2))
day = int(mo.group(4))
year = int(mo.group(6))


# April, June, September, and November have 30 days, February has 28 days, 
# and the rest of the months have 31 days.

def isDateValid(month, day, year):
    if month < 1 or month > 12:
        return False
    elif day < 0 or day > 31:
        return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day == 31:
            return False
    elif month == 2:
        if day > 29:
            return False
        elif day == 29  and year % 4 != 0 and (year % 100 != 0 or year % 400 == 0):
            return False
        elif day == 28 and year % 4 == 0 and (year % 100 == 0 and year % 400 != 0):
            return False
    return True

print(isDateValid(month, day, year))