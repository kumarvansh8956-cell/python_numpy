import numpy as np
arr1 = np.array([[1,2,3,5,6,8,9,9,],
                   [5,6,7,0,8,7,76,7]])
                   
print(np.sum(arr1))
print(np.mean(arr1))
print(np.max(arr1))
print(np.min(arr1))
print(np.std(arr1))
print(np.var(arr1))
print(np.median(arr1))
print(arr1.shape)
 #indexing

print(arr1[1,2])

#slicing arr[row_start:row_end:raw_step, col_start:col_end:column_step]
print(arr1[:99:2, :7:3])