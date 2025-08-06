import csv

with open('employees_data.csv', 'r', newline='') as csvfile:
    r_obj = csv.reader(csvfile)
    for row in r_obj:
        print(row)