countries = {"IN":"India",
             "CA":"Canada",
             "UK":"United Kingdom",
             "US":"United States",
             "AU":"Australia"}

print(countries['NZ'])

print(countries.get('NZ'))
print(countries.get('NZ', 'Unknown Key'))
