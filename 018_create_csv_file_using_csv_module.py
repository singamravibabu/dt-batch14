import csv

# create a list of lists with 5 rows and 3 columns
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago'],
    ['David', 40, 'Houston']
]

with open('employees_data.csv', 'w', newline='') as csvfile:
    w_obj = csv.writer(csvfile)
    w_obj.writerows(data)
    