import numpy as np

# to create a 1D array
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

# to create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:")
print(arr2)

# to create an array of zeros
zeros = np.zeros(5)
print("Zeros:", zeros)

# to create an array of ones
ones = np.ones(5)
print("Ones:", ones)

# to create a range of numbers
numbers = np.arange(1, 11)
print("Numbers:", numbers)


#array_indexing 

arr_index = np.array([10, 20, 30, 40, 50])
print("First element:", arr_index[0])
print("Third element:", arr_index[2])
print("Last element:", arr_index[-1])

#array_slicing

arr_slice = np.array([10, 20, 30, 40, 50, 60])
print("First three elements:", arr_slice[0:3])
print("Elements from index 2:", arr_slice[2:])
print("First four elements:", arr_slice[:4])
print("Every second element:", arr_slice[::2])

#array_broadcasting

arr_broadcast = np.array([10, 20, 30, 40])
print("Addition:", arr_broadcast + 5)
print("Multiplication:", arr_broadcast * 2)
print("Subtraction:", arr_broadcast - 5)