quote = "Failures are stepping stones to success"
words = quote.split()
print(words)

meeting_date = '25/8/2025'
parts_of_date = meeting_date.split('/')
print(parts_of_date)
['25', '8', '2025']
day = int(parts_of_date[0])
month = int(parts_of_date[1])
year = int(parts_of_date[2])
print(day)
print(month)
print(year)

address = "Pradeep|Door No. 12|Block B|Keerthi Apts|Road 12|Malkajgiri|Hyderabad|500047"
parts_of_address = address.split('|')
print(parts_of_address)
