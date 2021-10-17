#status : not understand
import numpy as np 
x = np.arange(0,10,2)
y = np.arange(5)
print(x)
print(y)
m = np.vstack([x,y])
print(m)
xy = np.hstack([x,y])
print(xy)

"""
>>> x = np.arange(0,10,2)
>>> y = np.arange(5)
>>> m = np.vstack([x,y])
>>> m
array([[0, 2, 4, 6, 8],
 [0, 1, 2, 3, 4]])
>>> 
>>> xy
array([0, 2, 4, 6, 8, 0, 1, 2, 3, 4])
"""