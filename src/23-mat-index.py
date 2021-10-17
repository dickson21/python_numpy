#indexing
import numpy as np  
a = np.arange(12).reshape(3,4)
print(a) 
i = np.array([[0, 1],[1, 2]]) # indices for the first dim of a
print(i)
j = np.array([[2, 1], [3, 3]]) # indices for the second dim of a
print(j)
print(a[i, j]) #[ [a(0,2) a(1,1)] [a(1,3) a(2,3)]] = [[2 5] [7 11]]
print(a[i,2])
print(a[:,j])

j = np.array([0,1])

#any row with col#1 to col#2 
#2x3 matrix = a col#0, col#1
print(a[:,j]) 
"""
[[0 1]
 [4 5]
 [8 9]]
"""

j = np.array([[0,1],[0,1]])
#3 x (2x2) matrix
# row#i with [[0,1],[0,1]] --> [[i/0,i/1],[i/0,i/1]] --> [[0 1][0 1]]
# row#0 with [[0,1],[0,1]] --> [[0/0,0/1],[0/0,0/1]] --> [[0 1][0 1]]
# row#1 with [[0,1],[0,1]] --> [[1/0,1/1],[1/0,1/1]] --> [[4 5][4 5]]
# row#2 with [[0,1],[0,1]] --> [[2/0,2/1],[2/0,2/1]] --> [[8 9][8 9]]
print(a[:,j]) 
"""
array([
[ 0, 1, 2, 3],
 [ 4, 5, 6, 7],
 [ 8, 9, 10, 11]])

[[[0 1]
  [0 1]]

 [[4 5]
  [4 5]]

 [[8 9]
  [8 9]]]
"""

j = np.array([[0,1],[2,3]])
print(a[:,j])
#3 x (2x2) matrix
# row#i with [[0,1],[2,3]] --> [[i/0,i/1],[i/2,i/3]]
# i=0 --> [[0 1][2 3]]
# i=1 --> [[4 5][6 7]]
# i=2 --> [[8 9][10 11]]
"""
array([
[ 0, 1, 2, 3],
 [ 4, 5, 6, 7],
 [ 8, 9, 10, 11]])

[[[ 0  1]
  [ 2  3]]

 [[ 4  5]
  [ 6  7]]

 [[ 8  9]
  [10 11]]]
"""
k1 = np.array([0,1]) #row index
k2 = np.array([2,3]) #col index
k = (k1,k2)
print(k)
print(a[k])
"""
a.array([
[ 0, 1, 2, 3],
 [ 4, 5, 6, 7],
 [ 8, 9, 10, 11]])

(array([0, 1]), array([2, 3]))
[a(0,2), a(1,3)]
[2 7]
"""



"""
>>> a = np.arange(12).reshape(3,4)
>>> a
array([
[ 0, 1, 2, 3],
 [ 4, 5, 6, 7],
 [ 8, 9, 10, 11]])
>>> i = np.array([[0, 1], # indices for the first dim of a
... [1, 2]])
>>> j = np.array([[2, 1], # indices for the second dim
... [3, 3]])
>>>
>>> a[i, j] # i and j must have equal shape
array([[ 2, 5],
 [ 7, 11]])
>>>
>>> a[i, 2]
array([[ 2, 6],
 [ 6, 10]])
>>>
>>> a[:, j] # i.e., a[ : , j]
array([[[ 2, 1],
 [ 3, 3]],
 [[ 6, 5],
 [ 7, 7]],
 [[10, 9],
 [11, 11]]])
>>> a[i,2]
 [[ 2  6]
 [ 6 10]]

>>> a[:,j]
 [[[ 2  1]
  [ 3  3]]

 [[ 6  5]
  [ 7  7]]

 [[10  9]
  [11 11]]]

[[0 1]
 [4 5]
 [8 9]]

[[[0 1]
  [0 1]]

 [[4 5]
  [4 5]]

 [[8 9]
  [8 9]]]


 [[[ 0  1]
  [ 2  3]]

 [[ 4  5]
  [ 6  7]]

 [[ 8  9]
  [10 11]]] 
 """