import re

mon = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
d = {1:'st',2:'nd',3:'rd'}

date = input("Enter a date in the format mm/dd/yy: ")
match = re.match('(\d\d)\/(\d\d)\/(\d\d\d\d)', date)

day = int(match.groups()[1])
month = int(match.groups()[0])
year = int(match.groups()[2])

month = mon[month-1]
if day in [1,21,31]:
    dp = d[1]
elif day in [2,22]:
    dp = d[2]
elif day in [3,23]:
    dp = d[3]
else:
    dp = 'th'

print("%s %d%s, %d" % (month, day, dp, year))
