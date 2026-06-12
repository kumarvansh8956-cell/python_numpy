'''
np.where()
find the element that satisfy a condition

'''
import numpy as np

arr = np.array([10, 20, 30, 40])

print(np.where(arr > 25))
# its also behave like condition flow

result = np.where(arr > 25, "Big", "Small")
print(result)
'''
np.unique()
it remove duolicate value and sorted them
'''
ar2 = np.array([3, 1, 2, 3, 2, 1])

print(np.unique(ar2))

'''
np.sort()
sorts the values
'''
ar3 = np.array([5, 1, 3, 2])

print(np.sort(ar3))

'''
np.argsort()
return the indices that wouid sort the array

'''
print(np.argsort(ar3))


'''
np.argmax()
return the indix of the greatest element in the array

'''
print(np.argmax(ar3))


'''
np.argmin()
return the indix of the smallest element in the array

'''
print(np.argmin(ar3))

'''
np.any(condition)
return true when at least one value is true or at leas one non-zero in array
'''
ar4 = np.array([0, 0, 5, 0])

print(np.any(ar4))

ar5 = np.array([True, False, True])

print(np.any(ar5))


'''
np.all(condition)
return true when all values are true or all values is non-zero in array
'''
print(np.all(ar4))
ar6 = np.array([True, True, True])

print(np.all(ar6))
# Random function

'''
np.random.rand(shape)
generate random floating number or array
shape default 1

'''

print(np.random.rand())

print(np.random.rand(4))

print(np.random.rand(2,5))

'''
np.random.randint(range,size = shape)
generate random integer number or array
no default
'''

print(np.random.randint(1,8,size=6))

print(np.random.randint(0,17,size=(4,2)))

'''
np.random.choice(size)
it randomly select one or more element from the array
default size = 1
'''
ar7 = [10,20,30,40]

np.random.choice(ar7)

np.random.choice(ar7,3)


'''
np.random.shuffle()

it Shuffles the original array.

'''
ar8 = np.array([1,2,3,4,5])

np.random.shuffle(ar8)

print(ar8)

'''
np.random.randn(size)

It generate one or more random numbers from a standard normal distribution.
default size = 1
'''
np.random.randn(5)

'''
. np.random.permutation()

It returns a shuffled copy.

'''
ar9 = np.array([1,2,3,4,5])

print(np.random.permutation(ar9))

'''
np.random.seed( value) 
it is used to make random numbers repeatable.
by this value will be fix no matter how many times we run the program
for each seed value the throwput is fixed
'''
np.random.seed(42)

print(np.random.randint(1,10,5))
np.random.seed(1)

print(np.random.randint(1,10,5))
np.random.seed(999)

print(np.random.randint(1,10,5))
