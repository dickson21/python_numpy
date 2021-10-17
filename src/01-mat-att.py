import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print("a.shape = " ,a.shape)
print("a.ndim = " , a.ndim)
print("a.dtype.name = ", a.dtype.name)
print("a.itemsize = ", a.itemsize)
print("a.size = ", a.size)
print("type(a) = ", type(a))
b = np.array([6, 7, 8])
print("b = " , b)
print("type(b) = ", type(b))

"""
### Output ####
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
a.shape =  (3, 5)
a.ndim =  2
a.dtype.name =  int32
a.itemsize =  4
a.size =  15
type(a) =  <class 'numpy.ndarray'>
b =  [6 7 8]
type(b) =  <class 'numpy.ndarray'>
"""