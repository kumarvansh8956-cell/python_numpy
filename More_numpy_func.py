import numpy as n

a = n.arange(1,11)
print(a)
print(a[[0,4,5,7,3]])
a2 = a.reshape(2,5)
print(a2)
print(a[a>5])
print(a2[a2>5])
print(a2.ravel())
print(a2.flatten())