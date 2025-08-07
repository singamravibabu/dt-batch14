import pickle

with open('books.dat', 'rb') as f:
    lst = pickle.load(f)
    for book in lst:
        print(book)
        