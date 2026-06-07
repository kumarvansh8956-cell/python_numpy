import numpy as n
'''
n.delete(Og_array,index,axis)
Og = original array
index = index of position where we need to insert the element

for 1-d
axis = NONE (default)
2-d
axis = 0 , delete a row, mean down the column
axis = 1 , delee a column, mean across the axis
for 3-d
axis = 0, block
axis = 1 , row
axis = 2 , column
 it does not modify the original array
 in n-d it remove entire list
'''

ar= n.array([1,2,3,4,5,6])
print(n.delete(ar,2))

ar1 = n.array([[1,2,3,4,5,6],[0,9,8,7,6,5]])
print(n.delete(ar1,0,axis=0))
print(n.delete(ar1,0,axis=1),"\n")

# stack function
'''
vstack((ar1,ar2)) = vertically stack (push)= row wise
hstack((ar1,ar2)) = horizontally stack (push) = column wise

'''
ar2 = n.array([1,5,6,78,7,8])
ar3 = n.array([9,4,4,78,5,4])
print(n.vstack((ar2,ar3)),"\n")
print(n.vstack((ar3,ar2)),"\n")
print(n.hstack((ar2,ar3)),"\n")
print(n.hstack((ar3,ar2)),"\n")


ar4 = n.array([[1,5,6,78],[1,9,7,5]])
ar5 = n.array([[9,4,4,7],[8,6,54,3]])

print(n.vstack((ar4,ar5)),"\n")
print(n.vstack((ar5,ar4)),"\n")
print(n.hstack((ar4,ar5)),"\n")
print(n.hstack((ar5,ar4)),"\n")

# split function

'''
split(ar, portion) = equal
vsplit(ar, portion) = vertically split = row wise
hsplit(ar, portion) = horizontally split  = column wise

'''


print(n.split(ar2,2),"\n")
print(n.split(ar3,2),"\n")
print(n.split(ar4,2),"\n")
print(n.split(ar5,2),"\n")


print(n.hsplit(ar4,2),"\n")
print(n.hsplit(ar5,2),"\n")
print(n.vsplit(ar4,2),"\n")
print(n.vsplit(ar5,2),"\n")
