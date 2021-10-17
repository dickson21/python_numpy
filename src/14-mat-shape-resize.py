
"""
The reshape function returns its argument with a modified shape, 
whereas the ndarray.resize method modifies the array itself:
"""
import numpy as np 
from numpy import random
a = np.floor(10* random.rand(3,4))  #random float
print(a)
a.resize((2,6))
print(a)
#If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:
a.reshape(3,-1)
print(a)

"""
[[8. 4. 9. 3.]
 [2. 5. 0. 0.]
 [6. 0. 4. 2.]]

[[8. 4. 9. 3. 2. 5.]
 [0. 0. 6. 0. 4. 2.]]
 
[[8. 4. 9. 3. 2. 5.]
 [0. 0. 6. 0. 4. 2.]]
"""