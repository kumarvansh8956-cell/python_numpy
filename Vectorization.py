#Vectorization means performing operations on an entire NumPy array at once instead of using Python loops.
# instead of this 
import numpy as np

list = [1,2,3,4]

result = []

for i in list:
    result.append(i * 2)

print(result)
# we simily does this
arr2 = np.array([[1,2,3],
                [4,5,6]])

print(arr2 + 10)

print(arr2 * 10)

