"""
These two functions return 
the indices of maximum and minimum elements respectively 
along the given axis.
"""

import numpy as np 
a = np.array([[30,40,70],[80,20,10],[50,90,60]]) 

print('Our array is:') 
print(a) 

print('Applying argmax() function:' )
print(np.argmax(a)) 

print('Index of maximum number in flattened array') 
print(a.flatten())
 
print('Array containing indices of maximum along axis 0:') 
maxindex = np.argmax(a, axis = 0) 
print(maxindex) 
 
print('Array containing indices of maximum along axis 1:') 
maxindex = np.argmax(a, axis = 1) 
print(maxindex) 

print('Applying argmin() function:') 
minindex = np.argmin(a) 
print(minindex)
 
print('Flattened array:') 
print(a.flatten()[minindex] )
 
print('Flattened array along axis 0:') 
minindex = np.argmin(a, axis = 0) 
print(minindex)

print('Flattened array along axis 1:') 
minindex = np.argmin(a, axis = 1) 
print(minindex)

"""
Our array is:
[[30 40 70]
 [80 20 10]
 [50 90 60]]
Applying argmax() function:
7
Index of maximum number in flattened array
[30 40 70 80 20 10 50 90 60]
Array containing indices of maximum along axis 0:
[1 2 0]
Array containing indices of maximum along axis 1:
[2 0 1]
Applying argmin() function:
5
Flattened array:
10
Flattened array along axis 0:
[0 1 1]
Flattened array along axis 1:
[0 2 0]
"""