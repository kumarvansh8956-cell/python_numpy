import numpy as np
# Matrix Multiplication

A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

print(A @ B)

# Dot Product
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.dot(a,b))
#Transpose
c = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(c.T)
# matrix power
print(np.linalg.matrix_power(c,2))
# trace
print(np.trace(A))

# rank
print(np.linalg.matrix_norm(c))
print(np.linalg.matrix_norm(A))

# solving linear equation
C = np.array([[2,1],
              [1,-1]])

D = np.array([5,1])

x = np.linalg.solve(C,D)

print(x)

#eigenvalues
print(np.linalg.eigvals(c))
# for both eignvalue and eignvector
E_Va , E_Ve = np.linalg.eig(c)
print(E_Va,"\n",E_Ve)
'''
eigh()

Works only for Hermitian/Symmetric matrices.
faster then eign

'''
A = np.array([[4,1],
              [1,3]])

values, vectors = np.linalg.eig(A)
print(values)
print(vectors)

#Inverse Matrix
G = np.array([[1,2],
              [3,4]])

print(np.linalg.inv(G))