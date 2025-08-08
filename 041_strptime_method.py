from datetime import date, time, datetime
dt1 = '2025-08-25'
dt1 = datetime.strptime(dt1, "%Y-%m-%d")
print(dt1)

dt2 = '10-16, 2005'
dt2 = datetime.strptime(dt2, "%m-%d, %Y")
print(dt2)

dt3 = "Tomorrow morning at 10 hours and 30 minutes, we will meet, don't for the date - 9th 08th month, 2025"
dt3 = datetime.strptime(dt3, "Tomorrow morning at %H hours and %M minutes, we will meet, don't for the date - %dth %mth month, %Y")
print(dt3)

dt4 = "8-16, 2025 @ 10:30 AM"
dt4 = datetime.strptime(dt4, "%m-%d, %Y @ %H:%M AM")
print(dt4)
