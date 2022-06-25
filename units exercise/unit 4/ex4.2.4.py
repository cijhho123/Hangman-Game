# כתבו תוכנית שמקבלת מהמשתמש תאריך במבנה dd/mm/yyyy ומדפיסה את היום בשבוע עבור התאריך שהוזן.

import calendar

print("Enter a date:")
date = input()

calendar.setfirstweekday(calendar.SUNDAY)

day = int(date[0:2])
month = int(date[4:5])
year = int(date[6:11])
print("day: ",day, "month: ", month, "year: ", year)

print(calendar.day_name[calendar.weekday(year, month, day)])