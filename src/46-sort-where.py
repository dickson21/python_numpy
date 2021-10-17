"""
The where() function returns the indices of elements in an input array 
where the given condition is satisfied
"""

import numpy as np 
x = np.arange(9.).reshape(3, 3) 

print('Our array is:') 
print(x) 

print('Indices of elements > 3') 
y = np.where(x > 3) 
print(y)  

print('Use these indices to get elements satisfying the condition') 
print(x[y])

"""
Our array is:
[[0. 1. 2.]
 [3. 4. 5.]
 [6. 7. 8.]]
Indices of elements > 3
(array([1, 1, 2, 2, 2], dtype=int64), array([1, 2, 0, 1, 2], dtype=int64))
Use these indices to get elements satisfying the condition
[4. 5. 6. 7. 8.]
"""