import numpy as np

# Create a 2D array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])
# Create a 1D array
array_1d = np.array([10, 20, 30])

# using broadcasting
result = array_2d + array_1d
# Print the result
print("Result of broadcasting:\n", result)