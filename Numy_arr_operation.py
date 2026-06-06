import numpy as np

Ar = np.array([[2,4,5], [7,8,9]])
print(Ar) # full array
print(Ar.shape) # shape of array in (raw,column)
print(Ar.size) # total no's of element
print(Ar.ndim) # dimination of array
print(Ar.dtype) # datatype
print(Ar[1][2]) # accessing of element
floot_Ar = Ar.astype(float)
print(floot_Ar)