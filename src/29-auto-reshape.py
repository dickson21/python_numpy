#status : not understand
import numpy as np 
a = np.arange(30)
b = a.reshape((2, -1, 3)) # -1 means "whatever is needed"
print(b.shape)

"""
>>> a = np.arange(30)
>>> b = a.reshape((2, -1, 3)) # -1 means "whatever is needed"
>>> b.shape
(2, 5, 3)
>>> b
array([[[ 0, 1, 2],
 [ 3, 4, 5],
 [ 6, 7, 8],
 [ 9, 10, 11],
 [12, 13, 14]],
 [[15, 16, 17],
 [18, 19, 20],
 [21, 22, 23],
 [24, 25, 26],
 [27, 28, 29]]])
 """