''''
NUMPY

N-Dimensional Array
Can quickly broadcast functions
Has Built-in linear algebra, statistical distributions, trigonomic and random number capabilities
'''
import numpy as np

# CREATING NUMPY ARRAYS
# This is a list of lists
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print(type(my_matrix))

# Making a LIST into an ARRAY. np.array
nump_matrix = np.array(my_matrix)
# print(np.array(my_matrix))
# print(type(nump_matrix))
'''NP.ARANGE'''
# NP.ARANGE 1 R. Give the input in terms of (start, stop, skze)  skze = skip size
# print(np.arange(0, 12, 3))

# print(np.random.rand(10))
print(np.random.seed(42))
# print(np.random.rand(4))

arr = np.arange(0, 50)

arr1 = np.arange(0, 11)
print(arr1)
print(arr1[8])
print(arr1[1:6:2])
print(arr1[:5])
print(arr1[0:5])

#BROADCASTING
arr1[0:5] = 100
print(arr1)

arr1 = np.arange(0, 11)
print(arr1)

slice_of_array = arr1[0:5]
print(slice_of_array)

# slice_of_array[:] = 99
# slice_of_array = 99
print(slice_of_array)
print(arr1)

arr1_copy = arr1.copy()
print(arr1_copy)
print(arr1)

arr1_copy[:] = 25
print(arr1_copy)
print(arr1)


# 2Dimensional Array

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)

#Grabbing single row. Working logic is ArrayName[Row, Column]
arr_2d.shape
print(arr_2d[2]) # For entire row
print(arr_2d[0,2]) #for number 15
print(arr_2d[1,1]) #for number 25

#SLICING. Working logic is ArrayName[ALL ROWS wanted, ALL COLUMNS wanted]
print(arr_2d[:2,1:])


#CONDITIONAL SELECTION
arr = np.arange(0,11)
arr > 4 #Comparison array
print(arr > 4) #Prints True to everything that matches the statement that the number in the array is larger than 4


bool_arr = arr>4 #Boolean Array
print(bool_arr)

arr[bool_arr] #Filter array
print(arr[bool_arr]) #Only returns whats applicable to the subject being printed but in value form not boolean


#Short version
print(arr[arr>4])

#Operations
arr25 = arr + 25
print(arr25)


arrsqrt = np.sqrt(arr)
print(arrsqrt)
print(arr_2d)

arr2d = np.arange(0,25).reshape(5,5)
print(arr2d)

arr2d.sum()
print(arr2d.sum())
print(arr.sum())
print(arr2d.sum(axis=0)) #axis = 0 --> Calculates counting the column total
print(arr2d.sum(axis=1)) #axis = 1 --> Calculates counting across the rows


#Exercises
arr10_5 = [10, 10, 10, 10, 10]
print(arr10_5)
arr10 = np.array(arr10_5)
print(type(arr10))

print(np.arange(10, 51))
print(np.arange(10, 51, 2))

arr3 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr3)
print(np.random.rand())
print(np.random.randn(26))
t_20 = np.arange(0,1, 20)

# RUN THIS CELL - THIS IS OUR STARTING MATRIX
mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:,1:])
print("Next")
print(mat[4:5])
print("Next")
print(mat[3:5])
print("Sum")
print(mat.sum())
print("Standard Deviation")
print(mat.std())
print("Column Sum")
print(mat.sum(axis=0))
print(np.random.randn(26))
print(np.random.randn(25))