#Indexing, Slicing and Iterating
import numpy as np  
a = np.arange(10)**3
print(a)
print(a[2])
print(a[2:5])
# equivalent to a[0:6:2] = 1000;
# from start to position 6, exclusive, set every 2nd element to 1000
a[:6:2] = 1000
print(a)
a[ : :-1]  
print(a)
for i in a:
   print(i**(1/3.))

"""
[  0   1   8  27  64 125 216 343 512 729]
8
[ 8 27 64]
[1000    1 1000   27 1000  125  216  343  512  729]
9.999999999999998
1.0
9.999999999999998
3.0
9.999999999999998
5.0
5.999999999999999
6.999999999999999
7.999999999999999
8.999999999999998
"""

