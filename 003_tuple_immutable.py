# tuple is immutable example
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10  # Attempt to modify the first element of the tuple
except TypeError as e:  # Catch the TypeError that occurs
    print(f"Error: {e}")