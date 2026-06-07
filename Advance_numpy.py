import numpy as n

'''
n.insert(Og_array,index,value,axis)
Og = original array
index = index of position where we need to insert the element
value = element ehich need to be insert
for 1-d
axis = NONE (default)
2-d
axis = 0 , insert row, mean down the column
axis = 1 , insert column, mean across the axis
for 3-d
axis = 0, block
axis = 1 , row
axis = 2 , column

inserting in 2-d and 3-d either
value must be single or same length of list as array

'''


 # for 1-D
ar = n.arange(0,10)
print(ar)
ar1 = n.arange(11,21)
print(ar1)

# for 2-D
ar2 = ar.reshape(2,5)
print(ar2)
print(n.insert(ar2,3,12))
ar3 = n.insert(ar2,2,12,axis=0)
print()
print(ar3)
print(n.insert(ar2,1,[1,1,3,0,0],axis=0))
print()
print(n.insert(ar2,2,12, axis=1))
print(n.insert(ar2,2,[99,6],axis=1))
'''
n.concatenate(array1,array2)
concatenate two array
note:- only same dimensions array can concatenate
'''
print(n.concatenate(ar,ar1))
print(n.concatenate(ar3,ar2))