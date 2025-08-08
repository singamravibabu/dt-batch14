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