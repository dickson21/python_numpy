#iterate the array
import numpy as np  
def f(x,y):
     return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
for row in b:print(row)

for element in b.flat:print(element)

"""
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]

0
1
2
.
.
43
"""

