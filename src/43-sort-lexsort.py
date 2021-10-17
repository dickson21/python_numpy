"""
function performs an indirect sort using a sequence of keys. 
The keys can be seen as a column in a spreadsheet. 
The function returns an array of indices, using which the sorted data can be obtained. 
Note, that the last key happens to be the primary key of sort.
"""

import numpy as np 

nm = ('raju','anil','ravi','amar') 
dv = ('f.y.', 's.y.', 's.y.', 'f.y.') 
ind = np.lexsort((dv,nm)) 

print('Applying lexsort() function:') 
print(ind)

print('Use this index to get sorted data:') 
print([nm[i] + ", " + dv[i] for i in ind]) 

"""
Applying lexsort() function:
[3 1 0 2]
Use this index to get sorted data:
['amar, f.y.', 'anil, s.y.', 'raju, f.y.', 'ravi, s.y.']
"""