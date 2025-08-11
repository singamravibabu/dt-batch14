countries = {"IN":"India",
             "CA":"Canada",
             "UK":"United Kingdom",
             "US":"United States",
             "AU":"Australia"}

del countries['AU']
print(countries)

countries.pop('US')

print(countries)

countries.clear()
print(countries)
