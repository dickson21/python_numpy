#image color
import numpy as np  
palette = np.array([[0, 0, 0], # black
 [255, 0, 0], # red
 [0, 255, 0], # green
 [0, 0, 255], # blue
 [255, 255, 255]]) # white
image = np.array([[0, 1, 2, 0], [0, 3, 4, 0]])
print(image)
print(palette[image]) # the (2, 4, 3) color image



"""
>>> palette = np.array([[0, 0, 0], # black
... [255, 0, 0], # red
... [0, 255, 0], # green
... [0, 0, 255], # blue
... [255, 255, 255]]) # white
>>> image = np.array([[0, 1, 2, 0], # each value corresponds to a color in the
 palette
... [0, 3, 4, 0]])
>>> palette[image] # the (2, 4, 3) color image
array([
[[ 0, 0, 0],
 [255, 0, 0],
 [ 0, 255, 0],
 [ 0, 0, 0]],

 [[ 0, 0, 0],
 [ 0, 0, 255],
 [255, 255, 255],
 [ 0, 0, 0]]])
 """