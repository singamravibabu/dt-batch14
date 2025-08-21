import numpy as np

arr = np.array([10, 20, 30, 40, 50])
# Accessing elements using slicing
print(arr[::2])  # Output: [10 30 50]

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr2d[[0, 2],
             [1, 2]])