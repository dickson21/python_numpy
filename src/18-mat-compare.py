#array reference
import numpy as np
a = np.array([[ 0, 1, 2, 3],
[ 4, 5, 6, 7],
[ 8, 9, 10, 11]])
b = a
print(b is a)



"""
>>> a = np.array([[ 0, 1, 2, 3],
... [ 4, 5, 6, 7],
... [ 8, 9, 10, 11]])
>>> b = a # no new object is created
>>> b is a # a and b are two names for the same ndarray object
True
"""