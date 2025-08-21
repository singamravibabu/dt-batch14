import numpy as np

arr = np.array([1, 2, 3])
arr_new = arr[np.newaxis, :] # Adding a new dimension at the beginning
print(arr_new.shape)  # Output: (1, 3)
print(arr_new)
arr_new_2 = arr[:, np.newaxis]  # Adding a new dimension at the end
print(arr_new_2.shape)  # Output: (3, 1)
print(arr_new_2)