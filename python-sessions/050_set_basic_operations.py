# creating a set
set_of_five_values = {1, 2, 3, 4, 5}

set_of_five_values.add(6)
print(set_of_five_values)

set_of_five_values.remove(6)
print(set_of_five_values)


set_of_five_values.update([6, 7, 8])
print(set_of_five_values)


set_of_five_values.discard(8)
print(set_of_five_values)

set_of_five_values.clear()
print(set_of_five_values)
