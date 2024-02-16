''''
NUMPY

N-Dimensional Array
Can quickly broadcast functions
Has Built-in linear algebra, statistical distributions, trigonomic and random number capabilities
'''
import numpy as np

# CREATING NUMPY ARRAYS
#This is a list of lists
my_matrix = [[1,2,3], [4,5,6], [7,8,9]]

print(type(my_matrix))


# Making a LIST into an ARRAY. np.array
nump_matrix = np.array(my_matrix)
print(np.array(my_matrix))
print(type(nump_matrix))
'''NP.ARANGE'''
# NP.ARANGE 1 R. Give the input in terms of (start, stop, skze)  skze = skip size
print(np.arange(0, 12, 3))


#print(np.random.rand(10))
#print(np.random.seed(42))
#print(np.random.rand(4))

arr = np.arange(0,50)
print(arr)
print(arr.reshape(10, 5))