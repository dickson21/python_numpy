import numpy as np
from numpy import pi

a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)
c = a+b
print(c)
d = np.exp(c*1j)
print(d)
print(d.dtype.name)

"""
float64
[1.         2.57079633 4.14159265]
[ 0.54030231+0.84147098j -0.84147098+0.54030231j -0.54030231-0.84147098j]
complex128
"""