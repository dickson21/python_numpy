# status : OK
# ref
"""
numpy.argmax() in Python
https://www.geeksforgeeks.org/numpy-argmax-python/

shape of array
https://www.w3schools.com/python/numpy_array_shape.asp


"""

import numpy as np 
time = np.linspace(20, 145, 5) # time scale
data = np.sin(np.arange(20)).reshape(5,4) # 4 time-dependent series
print(time)
print(data)
ind = data.argmax(axis=0) #axis=0:column 1:row
print(ind)
time_max = time[ind]
print(time_max)
print(data.shape)
print(data.shape[1])
print(range(data.shape[1]))
data_max = data[ind, range(data.shape[1])]
print(data_max)
data_max = data[ind, range(1,2)]
print(data_max)
data_max = data[[2,0,3,1], [0,1,2,3]] #data[2,0], data[0,1], data[3,2], data[1,3]
print(data_max)

"""
>>> time = np.linspace(20, 145, 5) # time scale
>>> data = np.sin(np.arange(20)).reshape(5,4) # 4 time-dependent series
>>> time
array([ 20. , 51.25, 82.5 , 113.75, 145. ])
>>> data
array([[ 0. , 0.84147098, 0.90929743, 0.14112001],
 [-0.7568025 , -0.95892427, -0.2794155 , 0.6569866 ],
 [ 0.98935825, 0.41211849, -0.54402111, -0.99999021],
 [-0.53657292, 0.42016704, 0.99060736, 0.65028784],
 [-0.28790332, -0.96139749, -0.75098725, 0.14987721]])
# index of the maxima for each series
>>> ind = data.argmax(axis=0)
>>> ind
array([2, 0, 3, 1])
# times corresponding to the maxima
>>> time_max = time[ind]
>>>
>>> data_max = data[ind, range(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...
>>> time_max
array([ 82.5 , 20. , 113.75, 51.25])
>>> data_max
array([0.98935825, 0.84147098, 0.99060736, 0.6569866 ])
>>> np.all(data_max == data.max(axis=0))
True
"""