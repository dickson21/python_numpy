
"""
Stacking together different arrays
"""
import numpy as np  
from numpy import random
a = np.floor(10*random.rand(2,2))
print(a)
"""
array([[9., 7.],
       [5., 2.]])
"""
b = np.floor(10*random.rand(2,2))
print(b)
"""
array([[1., 9.],
       [5., 1.]])
"""
print(np.vstack((a,b))) #4x2 matrix
"""
array([[9., 7.],
       [5., 2.],
       [1., 9.],
       [5., 1.]])
"""
print(np.hstack((a,b))) #2x4 matrix
"""
array([[9., 7., 1., 9.],
       [5., 2., 5., 1.]])
"""