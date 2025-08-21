import numpy as np

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr2d[0, 1]) # Output: 2
print(arr2d[1, -1]) # Output: 6
print(arr2d[1:3, 0:2]) # Output: [[4 5]
                        #          [7 8]]
print(arr2d[1:3, 0:2]) # Output: [[4 5] [7 8]]
print(arr2d[:, 1]) # Output: [2 5 8]