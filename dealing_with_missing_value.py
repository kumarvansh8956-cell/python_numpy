# nan = not a number (missing value, blank column, undefine data, invalid data)
''' In numpy nan is stands for Not A Number it represent missing value, blank column, undefine data, invalid data,etc
those value alot of trouble in data set and machine learning models
sytax = np.nan'''

import numpy as m
x = m.nan
print(x)
 # how and where it appear?
arr = m.array([3,4,m.nan,7,m.nan,67, 100, m.nan,1111])
print(arr)
# how to check nan in data?
''' we use "np.isnan()" function from numpy to detect if data have nan or not
if it does't contain nan it return FALSE otherwise TRUE.
important note:- we can't use this for camparing quantity of nan in dataset 

sytax :- np.isnan(array)
'''
print(m.isnan(m.nan))
print(m.isnan(arr))

# how to replace a nan with number?
''' we "np.nan_to_num()" function to replace the nan with a number.
syntax :- np.nan_to_num(array, nan = value)
default value for this function is 0. if you does not give the value then numpy  replace all nan with zero 0
it create new array so original array remaining untouched
'''
print(m.nan_to_num(arr))
print(m.nan_to_num(arr, nan = 10))

# how to deal with infinity?

''' np.inf represents positive infinity, a value greater than any finite floating-point number,
 while -np.inf represents negative infinity, a value smaller than any finite floating-point number.
 
 Infinity represents a value larger than any finite number.
 NumPy treats inf as a value larger than any finite number and -inf as smaller than any finite number.
 '''
x = m.inf
y = -m.inf
print( x ,"\n", y)

# how to detect the infinities?
''' we use "np.isinf()" function from numpy to detect if data have infinity or not
if it does't contain infinity it return FALSE otherwise TRUE.
important note:- we can't use this for camparing quantity of inf in dataset 
sytax :- np.isfin(array)
'''
arr2 = m.array([3 ,4 ,m.nan,7,-m.inf,67, 100, m.nan,m.inf])
print(m.isinf(arr2))

# how to replace a inf with number?
''' we "np.inf_to_num()" function to replace the nan with a number.
syntax :- np.nan_to_num(array, posinf = value, neginf = -value)
when you use functions like np.nan_to_num(), NumPy may replace
np.inf with the largest representable floating-point number for that data type.
'''
print(m.nan_to_num(arr2))
print(m.nan_to_num(arr2,posinf=100))
print(m.nan_to_num(arr2,neginf=-77))
print(m.nan_to_num(arr2,posinf=100,neginf=-100))