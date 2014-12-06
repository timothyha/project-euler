# https://projecteuler.net/problem=19
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September, / April, June and November. / All the rest have thirty-one, / Saving February alone, / Which has twenty-eight, rain or shine. / And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def dayinyear(y):
    result = 365
    if y%4 == 0: result = 366
    if y%100 == 0: result = 365
    if y%400 == 0: result = 366
    return result

dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def dayinmonth(m,y):
    global dim
    result = dim[m-1]
    if m==2: result = dayinyear(y)-365
    return result

def daysfrom1900(y,m,d):
    days = 0
    for yy in range(1900,y): days = days + dayinyear(yy)
    for mm in range(1,m): days = days + dayinmonth(mm,y)
    return days + d - 1

#print daysfrom1900(1900,1,31)
#print daysfrom1900(1900,3,31)
#print daysfrom1900(1900,3,1)

sundays = 0
for y in range(1901,2001):
    for m in range(1,13):
        days = daysfrom1900(y,m,1)
        if days%7 == 6:
            print y,m,1
            sundays = sundays + 1

print "Answer", sundays