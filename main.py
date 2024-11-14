# Import numpy
import numpy as np

# Creating a basic numpy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Creating a 2-D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# Check the dimensions of array
# Syntax: array_name.ndim
print(arr_2d.ndim)

# Print the shape of array
# Syntax: array_name.shape
print(arr_2d.shape)

# Creating a array filled with 0's
# Syntax: array_name = numpy.zeros((array shape))
zeros_arr = np.zeros((4, 5))
print(zeros_arr)




