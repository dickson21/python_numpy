import numpy as np
b = np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0)) # sum of each column
print(b.min(axis=1)) # min of each row
print(b.cumsum(axis=1))  # cumulative sum along each row

"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

 sum of each column
[12 15 18 21]

min of each row
[0 4 8]

cumulative sum along each row
[[ 0  1  3  6]
 [ 4  9 15 22]
 [ 8 17 27 38]]
"""
