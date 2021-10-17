#status : OK
#detail : transpose
"""
The ix_ (../reference/generated/numpy.ix_.html#numpy.ix_) function can be used to combine
dierent vectors so as to obtain the result for each n-uplet. For example, if you want to compute
all the a+b*c for all the triplets taken from each of the vectors a, b and c:
"""

import numpy as np  
a = np.array([2,3,4,5])
b = np.array([8,5,4])
c = np.array([5,4,6,8,3])
ax,bx,cx = np.ix_(a,b,c) #transpose
print(ax)
print(bx)
print(cx)
print( ax.shape, bx.shape, cx.shape)
result = ax+bx*cx
print(result)

#Method#1 : matrix multiply
print("Method#1 : matrix multiply - OK")
a1 = np.array([[1,2],[3,4]])
#print(a1)
b1 = np.array([[1],[1]])
#print(b1)
c1 = np.matmul(a1,b1)
print(c1)

#Method#2 : matrix multiply - OK
print("Method#2 : matrix multiply - OK")
a2 = np.array([[1,2],[3,4]])
#print(a2)
b2 = np.array([[1,1],[0,0]])
bx2 = np.transpose(b2)
#print(bx2)
#print(bx2[0,0])
b2t = np.array([[0],[0]])
b2t[0,0] = bx2[0,0]
b2t[1,0] = bx2[1,0]
#print(b2t)
c2 = np.matmul(a2,b2t)
print(c2)

#Method#3 : matrix multiply - OK
print("Method#3 : matrix multiply - OK")
a3 = np.array([[1,2],[3,4]])
#print(a3)
b3 = np.array([[1,1],[0,0]])
b4 = np.array([1,1])
bx3 = np.transpose(b3)
#print(bx3)
b3t = bx3[[0,1],[0,0]]
#print("b3t = " ,b3t)
b3x, temp = np.ix_(b3t, b3t)
#print(b3x)
c32 = np.matmul(a3,b3x)
print(c32)


#Method#4 : matrix multiply - OK
print("Method#4 : matrix multiply - OK")
a4 = np.array([[1,2],[3,4]])
#print(a4)
b4 = np.array([1,1])
b4x, temp = np.ix_(b4, b4)
#print(b4x)
c4 = np.matmul(a4,b4x)
print(c4)


"""
>>> a = np.array([2,3,4,5])
>>> b = np.array([8,5,4])
>>> c = np.array([5,4,6,8,3])
>>> ax,bx,cx = np.ix_(a,b,c)
>>> ax
array([[[2]],
 [[3]],
 [[4]],
 [[5]]])
>>> bx
array([[[8],
 [5],
 [4]]])
>>> cx
array([[[5, 4, 6, 8, 3]]])
>>> ax.shape, bx.shape, cx.shape
((4, 1, 1), (1, 3, 1), (1, 1, 5))
>>> result = ax+bx*cx
>>> result
array([[[42, 34, 50, 66, 26],
 [27, 22, 32, 42, 17],
 [22, 18, 26, 34, 14]],
 [[43, 35, 51, 67, 27],
 [28, 23, 33, 43, 18],
 [23, 19, 27, 35, 15]],
 [[44, 36, 52, 68, 28],
 [29, 24, 34, 44, 19],
 [24, 20, 28, 36, 16]],
 [[45, 37, 53, 69, 29],
 [30, 25, 35, 45, 20],
 [25, 21, 29, 37, 17]]])
>>> result[3,2,4]
17
>>> a[3]+b[2]*c[4]
17
Method#1 : matrix multiply - OK
[[3]
 [7]]
Method#2 : matrix multiply - OK
[[3]
 [7]]
Method#3 : matrix multiply - OK
[[3]
 [7]]
Method#4 : matrix multiply - OK
[[3]
 [7]]
"""