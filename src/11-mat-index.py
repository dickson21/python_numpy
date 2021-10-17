"""
dots (...) represent as many colons as needed to produce a complete indexing tuple
x[1,2,...] is equivalent to x[1,2,:,:,:],
x[...,3] to x[:,:,:,:,3] and
x[4,...,5,:] to x[4,:,:,5,:].
"""

import numpy as np 
# a 3D array (two stacked 2D arrays)
c = np.array( [[[  0,  1,  2],    
                 [ 10, 12, 13]],
                [[100,101,102],
                 [110,112,113]]])
print(c.shape)
# (2, 2, 3)
print(c[1,...])  # same as c[1,:,:] or c[1]
"""
array([[100, 101, 102],
       [110, 112, 113]])
"""
print(c[...,2] ) # same as c[:,:,2]
"""
array([[  2,  13],
       [102, 113]])
"""     
