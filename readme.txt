Subject : Numpy howto
Created : 2020-08-13
Author : dickson.cheng

01+ :  basic
11+ :  matrix operation
31+ :  histogram
40+ :  sort search counting


/* Ref */
/*******/
Numpy tutorial
mobile app

Complete Python NumPy Tutorial(Creating Arrays, Indexing, Math, Statistics, Reshaping)
youtube.com/watch?v=GB9ByFAIAH4

Numpy quickstart
https://numpy.org/doc/stable/user/quickstart.html
https://docs.scipy.org/doc/numpy-1.16.1/user/quickstart.html

NumPy: the absolute basics for beginners
https://numpy.org/doc/stable/user/absolute_beginners.html

NumPy tutorial
https://numpy.org/doc/stable/user/tutorials_index.html

NumPy howtos
https://numpy.org/doc/stable/user/howtos_index.html

NumPy routines
https://numpy.org/doc/stable/reference/routines.html

NumPy v1.19 Manual
https://numpy.org/doc/1.19/

Example code from [QuickStart tutorial- Numpy 1.19 manual.pdf]


/* Summary */
Question : basicxx.py {27}

/* Output */

>>> import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int64'
>>> a.itemsize
8
>>> a.size
15
>>> type(a)
<class 'numpy.ndarray'>
>>> b = np.array([6, 7, 8])
>>> b
array([6, 7, 8])
>>> type(b)
<class 'numpy.ndarray'>