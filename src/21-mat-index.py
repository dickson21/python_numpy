#indexing
import numpy as np  
a = np.arange(12)**2
print(a)
i = np.array([1, 1, 3, 8, 5])
print(a[i])
j = np.array([[3, 4], [9, 7]])
print(a[j])


"""
>>> a = np.arange(12)**2 # the first 12 square numbers
>>> i = np.array([1, 1, 3, 8, 5]) # an array of indices
>>> a[i] # the elements of a at the positions i
array([ 1, 1, 9, 64, 25])
>>>
>>> j = np.array([[3, 4], [9, 7]]) # a bidimensional array of indices
>>> a[j] # the same shape as j
array([[ 9, 16],
 [81, 49]])

[  0   1   4   9  16  25  36  49  64  81 100 121]
[ 1  1  9 64 25]
[[ 9 16]
 [81 49]] 
"""