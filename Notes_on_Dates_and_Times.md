# WORKING WITH DATES/TIMES
- We can create date, time, datetime values using contructs from `datetime` module.
- There are 3 constructs:
    - date(year, month, day)
    - time(hours, minutes, seconds, microseconds)
    - datetime(year, month, day, hours, minutes, seconds, microseconds)

- The strptime(datetime_str, format_str) method
    - The 'p' in strptime() stands for parsing
    - This method converts a string to datetime object
    - Format codes:
        d - day of a month (number),
        m - month of a year (number),
        y - two-digit year number
        Y - four-digit year number
        H - hour number (0-23)
        M - minute number (0-59)
        S - second number (0-59)
        f - microsecond number (0-999999)
        A - AM/PM
        a - am/pm
        % - literal % character

- strftime(format_str)
    - The 'f' in strftime() stands for formatting
    - This method converts a datetime object to string
    - Format codes:
        a - Short weekday name
        A - Full weekday name
        b - Short month name
        B - Full month name
        d - Day of the month (number)
        m - Month of the year (number)
        Y - four-digit year number
        y - two-digit year number
        H - Hour of the day (0-23)
        M - Minute of the hour (number)
        p - AM/PM
        S - Second of the minute (number)
        U - Microsecond (number)

#### WORKING WITH TIME SPANS
- The time spans in Python are called timedelta objects
- We can create timedelta objects using timedelta construct from datetime module
from datetime import timedelta
```
timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

Time detal object attributes and a method
- days - returns number of days
- seconds - returns number of seconds, after days
- microseconds - returns number of microseconds, after days, and seconds
- total_seconds() - total seconds


#### Attributes of datetime objects
- year - returns year
- month - returns month
- day - returns day
- hour - returns hour
- minute - returns minute
- microsecond - returns microsecond
