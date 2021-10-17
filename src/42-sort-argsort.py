"""
The numpy.argsort() function performs an indirect sort on input array, 
along the given axis and using a specified kind of sort to return the array of indices of data. 
This indices array is used to construct the sorted array.
"""

import numpy as np 
x = np.array([3, 1, 2]) 

print('Our array is:' )
print(x)
 

print('Applying argsort() to x:') 
y = np.argsort(x) 
print(y)


print('Reconstruct original array in sorted order:') 
print(x[y])


print('Reconstruct the original array using loop:')
for i in y: 
   print(x[i])

"""
Our array is:
[3 1 2]
Applying argsort() to x:
[1 2 0]
Reconstruct original array in sorted order:
[1 2 3]
Reconstruct the original array using loop:
1
2
3
"""   