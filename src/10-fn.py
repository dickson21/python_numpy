import numpy as np  
def f(x,y):
     return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
print(b)
print(b[2,3])
print(b[0:5, 1])  # each row in the second column of b
print(b[ : ,1])   # equivalent to the previous example
print(b[1:3, : ]) # each column in the second and third row of b



"""
[[ 0  1  2  3]
 [10 11 12 13]
 [20 21 22 23]
 [30 31 32 33]
 [40 41 42 43]]

 23

# each row in the second column of b
[ 1 11 21 31 41]
# each row in the second column of b
[ 1 11 21 31 41]

# each column in the second and third row of b
[[10 11 12 13]
 [20 21 22 23]]
 """