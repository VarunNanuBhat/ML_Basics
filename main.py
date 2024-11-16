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


# Generating random nos in numpy
# Import random module from numpy
from numpy import random

# Generate a 1-D array of size 10 containing  values between 1 to 10
rand_array = random.randint(10, size = (10))
print(rand_array)

# Random data distribution
random_data_dist = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(random_data_dist)