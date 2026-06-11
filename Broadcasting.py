# problem
prices = [200,400,490,2200,600,760]
discount = 10 # 10% 
final_prices = []
for price in prices:
  final_price = price - (price*(discount/100))
  final_prices.append(final_price)
  print(final_price)

print(final_prices)
''' lengthy program
slow processing for large dataset
high time complexity
'''
# by numpy broadcasting help
import numpy as n
pr1 = n.array( [200,400,490,2200,600,760])
disc = 10
pr2 = pr1 - (pr1*(disc/100))
print(pr2)
'''
less line of codes
eas programming
faster then loops
better for large size array
'''
#  rule of Broadcasting
'''Rules
1. Compare shapes from right to left.
2. Two dimensions are compatible if:
     They are equal, or
     One of them is 1.
3. Missing dimensions are treated as 1.
4. If any dimension is incompatible, NumPy raises a ValueError.'''


#Compare shapes from right to left.
arr1 = n.array([[1,2,3],
                   [5,6,7]])
arr2 = n.array([[9,6,4],
                   [6,4,5]])
#Two dimensions are compatible if:
  #They are equal, 
print(arr1+arr2)
print()
  #one of them is 1.
arr3 = n.array([9,6,4])
print(arr1+arr3)
'''[9,6,4]+[1,2,3],
                   [5,6,7]+[9,6,4]'''
#Missing dimensions are treated as 1.
#If any dimension is incompatible, NumPy raises a ValueError.
arr4 = n.array([9,6])# if we applies any funtion it give value error
'''solve this using reshape function'''
arr5 = n.reshape(arr1,(3,2))
print(arr5)
print(arr4+arr5)