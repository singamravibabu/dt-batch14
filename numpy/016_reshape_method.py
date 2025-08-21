import numpy as np

arr = np.arange(24)
# print(arr)
arr_4x6 = arr.reshape(4, 6)
print(arr_4x6)
arr_8x3 = arr.reshape(8, 3)
# print(arr_8x3)
arr_3x2x4 = arr.reshape(3, 2, 4)
# print(arr_3x2x4)
arr_flattened = arr_4x6.flatten()
print(arr_flattened)