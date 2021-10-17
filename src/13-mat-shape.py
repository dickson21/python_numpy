"""
shape manipulate
The shape of an array can be changed with various commands. 
Note that the following three commands all return a modified array, 
but do not change the original array:

"""
import numpy as np  
from numpy import random
a = np.floor(10* random.rand(3,4))  #random float
print(a)
print(a.shape)
print(a.ravel())  # returns the array, flattened
print(a.reshape(6,2))  # returns the array with a modified shape
print(a.T)  # returns the array, transposed
print(a.T.shape)
print(a.shape)

"""
original array
[[9. 0. 4. 5.]
 [8. 9. 5. 2.]
 [9. 0. 2. 2.]]

array shape
(3, 4)

flat array
[9. 0. 4. 5. 8. 9. 5. 2. 9. 0. 2. 2.]

reshape array
[[9. 0.]
 [4. 5.]
 [8. 9.]
 [5. 2.]
 [9. 0.]
 [2. 2.]]

array transpose
[[9. 8. 9.]
 [0. 9. 0.]
 [4. 5. 2.]
 [5. 2. 2.]]

(4, 3)
(3, 4)

(4, 3)
(3, 4)
"""

