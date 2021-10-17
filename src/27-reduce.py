#status : Not Understand
import numpy as np  



"""
>>> def ufunc_reduce(ufct, *vectors):
... vs = np.ix_(*vectors)
... r = ufct.identity
... for v in vs:
... r = ufct(r,v)
... return r


>>> ufunc_reduce(np.add,a,b,c)
array([[[15, 14, 16, 18, 13],
 [12, 11, 13, 15, 10],
 [11, 10, 12, 14, 9]],
 [[16, 15, 17, 19, 14],
 [13, 12, 14, 16, 11],
 [12, 11, 13, 15, 10]],
 [[17, 16, 18, 20, 15],
 [14, 13, 15, 17, 12],
 [13, 12, 14, 16, 11]],
 [[18, 17, 19, 21, 16],
 [15, 14, 16, 18, 13],
 [14, 13, 15, 17, 12]]])
 """