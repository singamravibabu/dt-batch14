import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
print(mask)  # Output: [False False False  True  True]
print(arr[mask])  # Output: [4 5]