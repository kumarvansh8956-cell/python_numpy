import numpy as n

a1 = n.arange(1,97) # 1-D
print(a1)
print(a1[1:25:4])
a2 = a1.reshape(6,16)
print(a2[:7:2,1:17:2])
a3 = a1.reshape(3,2,16)
print(a3)
print(a3[0:3:3,1:2,0:12:3])