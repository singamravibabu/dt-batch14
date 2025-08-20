# create a list of seven data science modules
data_science_modules = [
    "Python for Data Science",
    "Data Manipulation with Pandas",
    "Data Visualization with Matplotlib",
    "Machine Learning with Scikit-Learn",
    "Deep Learning with TensorFlow",
    "Natural Language Processing with NLTK",
    "Big Data Analytics with Spark"
]

with open("data_science_modules.txt", "w") as file:
    for module in data_science_modules:
        module = module + "\n"
        file.write(module)


# a list of five years starting from 2015
years = [2015, 2016, 2017, 2018, 2019]
with open("years.txt", "w") as file:
    for year in years:
        file.write(str(year) + "\n")