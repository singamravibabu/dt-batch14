countries = {"IN":"India",
             "CA":"Canada",
             "UK":"United Kingdom",
             "US":"United States",
             "AU":"Australia"}

print(countries)

print(countries['IN'])

print(countries['AU'])

countries['JP'] = 'Japan'
print(countries)

countries['UK'] = "Ucranine"
print(countries)

##### get() method of dictionaries
dict_name.get(key, [default_value])
