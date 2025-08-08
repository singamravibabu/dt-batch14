from datetime import date, time, datetime
print(date.today())     # today's date

print(datetime.now())   # current date and time

print(datetime.now())   # current date and time


# constructing dates
# date(year, month, day)
meeting_day = date(2025, 8, 25)
print(meeting_day)


# constructing time values: time(hour, minute, second, microsecond)
login_time = time(10,30,0)
print(login_time)

# constructing datetime objects: datetime(year, month, day[, hours][, minutes][, seconds][, microseconds])
special_meet = datetime(2025, 10, 15, 16, 45, 0)
print(special_meet)
