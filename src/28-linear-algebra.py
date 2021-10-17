#status : OK
"""
ref : 
numpy.linalg.inv() function to calculate the inverse of a matrix
numpy.linalg.solve() function gives the solution of linear equations in the matrix form

numpy.linalg.inv()
https://www.tutorialspoint.com/numpy/numpy_inv.htm

numpy.linalg.solve()
https://www.tutorialspoint.com/numpy/numpy_solve.htm

numpy.linagl.eig()
Compute the eigenvalues and right eigenvectors of a square array.

Introduction to Eigenvalues and Eigenvectors - Part 1
https://www.youtube.com/watch?v=G4N8vJpf7hM

"""

import numpy as np 
A = np.array([[1.0, 2.0], [3.0, 4.0]])
print(A)
A.transpose()
AInv = np.linalg.inv(A)
u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
print(u)
c = np.matmul(AInv ,A)
print(c)
print(np.dot(A,AInv))

C = np.array([[5.], [7.]])
X = np.linalg.solve(A, C) #AX = C --> A* x A x X = A* x C --> IX = A* x C --> X = A* x C
print("AX = C ; X =  ", X)

print("Method#1")
B = np.array([[3, 0], [1, 2]])
print(B)
x1 = np.array([0,1])
print(np.dot(B,x1))
print("B matrix : egivalue=2, egivector=[0,1]")
x2 = np.array([0.7071, 0.7071])
print(np.dot(B,x2))
print("B matrix : egivalue=3, egivector=[0.7071,0.7071]")

print("Method#2")
w2,v2 = np.linalg.eig(B)
print("egivalues = ", w2) #egivalues
print("egivectors = ", v2) #egivector
print("verify")
print("B x v2" , np.dot(B,v2)) #result = v2.col0 x 2  v2.col1 x 3


"""
>>> import numpy as np
>>> a = np.array([[1.0, 2.0], [3.0, 4.0]])
>>> print(a)
[[1. 2.]
 [3. 4.]]
>>> a.transpose()
array([[1., 3.],
 [2., 4.]])
>>> np.linalg.inv(a)
array([[-2. , 1. ],
 [ 1.5, -0.5]])
>>> u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
>>> u
array([[1., 0.],
 [0., 1.]])
>>> j = np.array([[0.0, -1.0], [1.0, 0.0]])
>>> j @ j # matrix product
array([[-1., 0.],
 [ 0., -1.]])
>>> np.trace(u) # trace
2.0
>>> y = np.array([[5.], [7.]])
>>> np.linalg.solve(a, y)
array([[-3.],
 [ 4.]])
>>> np.linalg.eig(j)
(array([0.+1.j, 0.-1.j]), array([[0.70710678+0.j , 0.70710678-0.j ],
 [0. -0.70710678j, 0. +0.70710678j]]))
>>>
Parameters:
 square matrix
Returns
 The eigenvalues, each repeated according to its multiplicity.
 The normalized (unit "length") eigenvectors, such that the
 column ``v[:,i]`` is the eigenvector corresponding to the
 eigenvalue ``w[i]`` .

[[1. 2.]
 [3. 4.]]
[[1. 0.]
 [0. 1.]]
[[1.0000000e+00 4.4408921e-16]
 [0.0000000e+00 1.0000000e+00]]
[[1.00000000e+00 1.11022302e-16]
 [0.00000000e+00 1.00000000e+00]]
AX = C ; X =   [[-3.]
 [ 4.]]
Method#1
[[3 0]
 [1 2]]
[0 2]
B matrix : egivalue=2, egivector=[0,1]
[2.1213 2.1213]
B matrix : egivalue=3, egivector=[0.7071,0.7071]

Method#2
egivalues =  [2. 3.]
egivectors =  [
 [0.         0.70710678]
 [1.         0.70710678]]

verify
B x v2 = w2 x v2
[[0 x 2 = 0.             0.7071 x 3 = 2.1213]
 [1 x 2 = 2.             0.7071 x 3 = 2.1213]]


"""