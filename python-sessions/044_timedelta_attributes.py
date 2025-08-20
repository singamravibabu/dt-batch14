from datetime import datetime, timedelta
project_duration = timedelta(weeks=2, days=4)
print(project_duration.days)   # days attribute

print(project_duration.seconds) # no seconds

daily_hours = timedelta(hours=8, minutes=30, seconds=0)
print(daily_hours.seconds)      # prints seconds

print(daily_hours.microseconds) # no microseconds

print(project_duration.total_seconds()) # total seconds
