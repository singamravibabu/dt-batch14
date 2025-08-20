import pickle

books = [
    ["To Kill a Mockingbird", "Harper Lee", 1960],
    ["1984", "George Orwell", 1949],
    ["The Great Gatsby", "F. Scott Fitzgerald", 1925],
    ["The Catcher in the Rye", "J.D. Salinger", 1951],
    ["Pride and Prejudice", "Jane Austen", 1813],
]

# Open a binary file for writing
with open("books.dat", "wb") as file:
    pickle.dump(books, file)