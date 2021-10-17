# View or Shallow Copy
import numpy as np  
a = np.array([ [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
c = a.view()
print(c is a) #false
print(c.base is a)  # true : c is a view of the data owned by a
print(c.flags.owndata) #false
c = c.reshape((2, 6))
print(c.shape)
print(a.shape)

s = a[ : , 1:3] #extract colume 1 to 3
print(s)
s[:] = 10 
print(a)

#deep copy
d = a.copy()
print(d is a) #false
d[0,0] = 999
print(a)

a = np.arange(int(1e8))
b = a[:100].copy()
del a




"""
>>> c = a.view()
>>> c is a
False
>>> c.base is a # c is a view of the data owned by a
True
>>> c.flags.owndata
False
>>>
>>> c = c.reshape((2, 6)) # a's shape doesn't change
>>> a.shape
(3, 4)
>>> c[0, 4] = 1234 # a's data changes
>>> a
array([[ 0, 1, 2, 3],
 [1234, 5, 6, 7],
 [ 8, 9, 10, 11]])

>>> s = a[ : , 1:3] # spaces added for clarity; could also be written "s = a[:, 1:
3]"
>>> s[:] = 10 # s[:] is a view of s. Note the difference between s = 10 and
 s[:] = 10
>>> a
array([[ 0, 10, 10, 3],
 [1234, 10, 10, 7],
 [ 8, 10, 10, 11]])

 #deep copy
 >>> d = a.copy() # a new array object with new data is create
d
>>> d is a
False
>>> d.base is a # d doesn't share anything with a
False
>>> d[0,0] = 9999
>>> a
array([[ 0, 10, 10, 3],
 [1234, 10, 10, 7],
 [ 8, 10, 10, 11]])

 >>> a = np.arange(int(1e8))
>>> b = a[:100].copy()
>>> del a # the memory of ``a`` can be released.

"""