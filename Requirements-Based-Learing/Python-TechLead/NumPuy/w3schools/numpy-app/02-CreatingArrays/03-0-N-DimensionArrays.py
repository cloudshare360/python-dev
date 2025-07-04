import numpy as np

# Zero Dimension Arrays
array = np.array(42)

print(array)


# One Dimension Arrays

'''
Yes, you can absolutely create multiple values.

The statement "Each value in an array is a 0-D array" means that when you have an array, like `[1, 2, 3]`, each individual number (1, 2, and 3) can be considered a 0-dimensional array or a scalar. It doesn't mean you can only have one value.

Think of it this way:

* **A single value:** `5` (This is a 0-D array/scalar)
* **Multiple values in a list/array:** `[5, 10, 15]` (This is a 1-D array, containing three 0-D arrays/scalars)

So, in any programming language or data structure, you can always create and work with multiple values, whether they are stored individually or grouped together in larger arrays/lists/collections.
'''

# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
#These are the most common and basic arrays.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

#2-D Arrays
#An array that has 1-D arrays as its elements is called a 2-D arra
# These are often used to represent matrix or 2nd order tensors.
# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
#Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#3-D arrays
#An array that has 2-D arrays (matrices) as its elements is called 3-D array.
#These are often used to represent a 3rd order tensor.
#Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)