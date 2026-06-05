# introduction with numpy array
import numpy as n
# 1-D array
num_arr = n.array([1,2,3,45,5,6,7])
print(num_arr) # print
print(num_arr[0]) # accessing element
print(num_arr.shape)
print(num_arr.ndim)
print(num_arr.size)
print(num_arr.dtype)
    
# 2-D array
Np_2D = n.array([[1,2,3],
                [4,5,6]])
print(Np_2D)
print(Np_2D[1][2])
print(Np_2D.shape)
print(Np_2D.ndim)
print(Np_2D.size)
print(Np_2D.dtype)
    
# 3-d array
Np_3D = n.array([[[1,3,2],
                 [4,5,6],
                 [7,8,9]],
                  [[3,45,6],
                  [8,6,5],
                  [6,7,8]]])
print(Np_3D)
print(Np_3D[1][2][2])
'''
arr[block][row][column]
       OR
arr[block, row, column]

'''
print(Np_3D.shape)
print(Np_3D.ndim)
print(Np_3D.size)
print(Np_3D.dtype)
# zeros matrix
d = n.zeros((2,3))
print(d)
# ones matrix
v = n.ones((2,2))
print(v)
#identical matrix
print(n.eye(3))

# range matrix
Ran1 = n.arange(0,12)
Ran2 = n.arange(0,11,2)

print(Ran1)
print(Ran2)

# reashape
print(Ran1.reshape(6,2))