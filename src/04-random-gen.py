import numpy as np
from numpy import random
#rg = np.random.default_rng(1)     # create instance of default random number generator
a = np.ones((2,3), dtype=int)
#b = rg.random((2,3))
b = random.rand(2,3)  #random float
a *= 3
print(a)
b += a
print(b)
#a += b  # b is not automatically converted to integer type

"""
[[3 3 3]
 [3 3 3]]
[[3.80191607 3.41074846 3.98227765]
 [3.62843185 3.66918514 3.82201946]]
"""
