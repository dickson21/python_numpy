import numpy as np   

B = np.arange(3)
print(B)
print(np.exp(B))
print(np.sqrt(B))
C = np.array([2., -1., 4.])
print(C)
D = np.add(B, C)
print(D)

"""
B = [0 1 2]
exp = [1.         2.71828183 7.3890561 ]
sqrt = [0.         1.         1.41421356]
C = [ 2. -1.  4.]
D = [2. 0. 6.]
"""