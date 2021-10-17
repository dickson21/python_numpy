import numpy as np
from numpy import pi
a = np.ones( (2,3,4), dtype=np.int16 )  
"""
[[[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]

 [[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]]
"""

a = np.empty( (2,3) )  
"""
[[6.23042070e-307 1.29060531e-306 1.37962320e-306]
 [1.29060871e-306 1.78022342e-306 2.33423131e-312]]  
"""
a = np.arange( 10, 30, 5 ) # get 5 number from 10 to 30
#[10 15 20 25]
a = np.arange(0,1,0.2)  # 9 numbers from 0 to 2 
#[0.  0.2 0.4 0.6 0.8]
a = np.linspace( 0, 2, 9 ) # useful to evaluate function at lots of points
#[0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]
x = np.linspace( 0, 2*pi, 10 )  # useful to evaluate function at lots of points
f = np.sin(x)
"""
[ 0.00000000e+00  6.42787610e-01  9.84807753e-01  8.66025404e-01
  3.42020143e-01 -3.42020143e-01 -8.66025404e-01 -9.84807753e-01
 -6.42787610e-01 -2.44929360e-16]
"""
#print(f)

a = np.arange(6) #1d array
# [0 1 2 3 4 5]

a = np.arange(12).reshape(4,3)  # 2d array
"""
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
"""

a = np.arange(24).reshape(2,3,4)         # 3d array
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
"""

print(np.arange(10000))  #short notation print
#np.set_printoptions(threshold=sys.maxsize) 
#[   0    1    2 ... 9997 9998 9999]
print(a)


