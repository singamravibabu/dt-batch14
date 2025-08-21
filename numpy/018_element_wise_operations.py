import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise addition
result_add = arr1 + arr2
# Element-wise subtraction
result_sub = arr1 - arr2
# Element-wise multiplication
result_mul = arr1 * arr2
# Element-wise division
result_div = arr1 / arr2
# Element-wise exponentiation
result_pow = arr1 ** arr2
# Element-wise exponentiation
result_pow_2 = arr1 ** 2

# Printing the results
print("Element-wise addition:", result_add)
print("Element-wise subtraction:", result_sub)
print("Element-wise multiplication:", result_mul)
print("Element-wise division:", result_div)
print("Element-wise exponentiation:", result_pow)
print("Element-wise exponentiation (squared):", result_pow_2)