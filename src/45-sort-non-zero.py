"""
The numpy.nonzero() function returns the indices of non-zero elements in the input array.
"""


import numpy as np 
a = np.array([[30,40,0],[0,20,10],[50,0,60]]) 

print('Our array is:')
print(a)   

print('Applying nonzero() function:') 
print(np.nonzero(a))

"""
Our array is:
[[30 40  0]
 [ 0 20 10]
 [50  0 60]]
Applying nonzero() function:
(array([0, 0, 1, 1, 2, 2], dtype=int64), array([0, 1, 1, 2, 0, 2], dtype=int64))
"""

