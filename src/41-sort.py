

import numpy as np  
a = np.array([[3,7],[9,1]]) 

print('Our array is:') 
print(a)


print('Applying sort() function:') 
print(np.sort(a)) 

print('Sort along axis 0:')
print(np.sort(a, axis = 0) )
 
# Order parameter in sort function 
dt = np.dtype([('name', 'S10'),('age', int)]) 
a = np.array([("raju",21),("anil",25),("ravi", 17), ("amar",27)], dtype = dt) 

print('Our array is:') 
print(a) 

print('Order by name:')
print(np.sort(a, order = 'name'))

"""
Our array is:
[[3 7]
 [9 1]]
Applying sort() function:
[[3 7]
 [1 9]]
Sort along axis 0:
[[3 1]
 [9 7]]
Our array is:
[(b'raju', 21) (b'anil', 25) (b'ravi', 17) (b'amar', 27)]
Order by name:
[(b'amar', 27) (b'anil', 25) (b'raju', 21) (b'ravi', 17)]
"""