years = []

with open('years.txt', 'r') as file:
    for year in file:
        year = year.replace('\n', '')
        year = int(year)  # Remove newline character
        years.append(year)

print(years)

#