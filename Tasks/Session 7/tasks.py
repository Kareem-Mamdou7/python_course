import numpy as np

letters = np.array([chr(i) for i in range(ord("a"), ord("k"))])

print("Array:", letters)
print("Dtype of array:", letters.dtype)
print("Shape of array:", letters.shape)
print("Size of array:", letters.size)

print("#" * 50)
even_array = np.arange(2, 33, 2).reshape(4, 4)
print("Even array with arange:\n", even_array)

print("#" * 50)
array_5x5 = np.arange(1, 26).reshape(5, 5)
print("Original 5x5 array:\n", array_5x5)

odd_numbers = array_5x5[array_5x5 % 2 == 1]
print("Odd numbers in the array:\n", odd_numbers)
