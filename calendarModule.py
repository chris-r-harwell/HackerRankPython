#!/bin/env python3
#
# REF: https://docs.python.org/3/library/calendar.html#calendar.TextCalendar
#

import calendar

# Read date input, splitting up on spaces.
month, day, year = map(int, input().split())

# Sunday is 0.
calendar.setfirstweekday(calendar.SUNDAY)

# For the above given date,
# get the day of the week, convert to a name
# and print it in all capital letters.
day_number = calendar.weekday(year, month, day)
day_name = calendar.day_name[day_number]
print(day_name.upper())
