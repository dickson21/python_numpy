#  identifier of an object
import numpy as np 
a = np.array([ 0, 1, 2, 3])
def f(x):
  print(id(x))

print(id(a))
f(a)


"""
>>> def f(x):
... print(id(x))
...
>>> id(a) # id is a unique identifier of an object
148293216 # may vary
>>> f(a)
148293216 # may vary
"""