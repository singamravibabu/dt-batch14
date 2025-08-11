from datetime import datetime

a_imp_day = datetime(2025, 10, 15)
print(a_imp_day.strftime("(%A) %b %d, %Y"))

print(a_imp_day.strftime("%Y - %B %d (%a)"))

a_meeting_dt = datetime(2025, 10, 15, 6, 30)
dt1 = a_meeting_dt.strftime("%H:%M:%S %p - %b %d, %Y")
print(dt1)

dt1 = a_meeting_dt.strftime("Time: %H:%M:%S %p \nDate: %b %d, %Y")
print(dt1)
