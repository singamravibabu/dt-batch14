import numpy as np

arr = np.array([1.2, 3.4, 5.6, 7.8])
print("Original array:", arr.dtype)

arr_int = arr.astype(np.int32)
print("New array:", arr_int.dtype)
