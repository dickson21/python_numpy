
"""
The extract() function returns the elements satisfying any condition.
"""

import numpy as np 
x = np.arange(9.).reshape(3, 3) 

print('Our array is:') 
print(x) 

# define a condition 
condition = np.mod(x,2) == 0 

print('Element-wise value of condition') 
print(condition)  

print('Extract elements using condition')
print(np.extract(condition, x))

"""
Our array is:
[[0. 1. 2.]
 [3. 4. 5.]
 [6. 7. 8.]]
Element-wise value of condition
[[ True False  True]
 [False  True False]
 [ True False  True]]
Extract elements using condition
[0. 2. 4. 6. 8.]
"""