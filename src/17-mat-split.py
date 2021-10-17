
import numpy as np
from numpy import random

a = np.floor(10*random.rand(2,12))
print(a)
# Split a into 3
b = np.hsplit(a,3)
print(b)


"""
>>> a = np.floor(10*rg.random((2,12)))
>>> a
array([[6., 7., 6., 9., 0., 5., 4., 0., 6., 8., 5., 2.],
 [8., 5., 5., 7., 1., 8., 6., 7., 1., 8., 1., 0.]])
# Split a into 3
>>> np.hsplit(a,3)
[array([[6., 7., 6., 9.],
 [8., 5., 5., 7.]]), array([[0., 5., 4., 0.],
 [1., 8., 6., 7.]]), array([[6., 8., 5., 2.],
 [1., 8., 1., 0.]])]
# Split a after the third and the fourth column
>>> np.hsplit(a,(3,4))
[array([[6., 7., 6.],
 [8., 5., 5.]]), array([[9.],
 [7.]]), array([[0., 5., 4., 0., 6., 8., 5., 2.],
 [1., 8., 6., 7., 1., 8., 1., 0.]])]

"""