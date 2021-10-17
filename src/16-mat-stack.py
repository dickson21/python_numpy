
import numpy as np 
from numpy import newaxis
from numpy import random
a = np.floor(10*random.rand(2,2))
b = np.floor(10*random.rand(2,2))
print(np.column_stack((a,b)))     # with 2D arrays
"""
array([[9., 7., 1., 9.],
       [5., 2., 5., 1.]])
"""
a = np.array([4.,2.])
b = np.array([3.,8.])
print(np.column_stack((a,b))) # returns a 2D array
"""
array([[4., 3.],
       [2., 8.]])
"""
print(np.hstack((a,b)))   # the result is different
"""
array([4., 2., 3., 8.])
"""
print(a[:,newaxis])  # view `a` as a 2D column vector
"""
array([[4.],
       [2.]])
"""
print(np.column_stack((a[:,newaxis],b[:,newaxis])))
"""
array([[4., 3.],
       [2., 8.]])
"""
print(np.hstack((a[:,newaxis],b[:,newaxis])))   # the result is the same
"""
array([[4., 3.],
       [2., 8.]])
"""
np.column_stack is np.hstack #false
np.row_stack is np.vstack #true

#creating row array
np.r_[1:4,0,4]
# array([1, 2, 3, 0, 4])
print(np.c_[np.array([1,2,3]), np.array([4,5,6])])
"""
[[1 4]
 [2 5]
 [3 6]]
"""

print(np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])])
"""
[[1 2 3 0 0 4 5 6]]
"""

"""
#np.column_stack((a,b))
[[5. 6. 8. 1.]
 [8. 5. 5. 6.]]


[[4. 3.]
 [2. 8.]]
[4. 2. 3. 8.]
[[4.]
 [2.]]
[[4. 3.]
 [2. 8.]]
[[4. 3.]
 [2. 8.]]
 """