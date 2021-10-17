import numpy as np

student1 = np.dtype([('name','S20'),('age', 'i1'),('mark','<f4')])
a = np.array([('ann', 10, 21.1),('bell', 11, 22.2),('carol', 12, 23.3)], dtype=student1)
print("student1")
print(a)

student2 = np.dtype([('id','i'),('age', 'i1'),('mark','<f4')])
a2 = np.array([('1', 10, 21),('2', 11, 22),('3', 12, 23)], dtype=student2)
print("student2")
print(a2)

student3 = np.dtype([('name',np.unicode_, 16),('age', 'i1'),('mark','<f4')])
a3 = np.array([('ann', 10, 21.1),('bell', 11, 22.2),('carol', 12, 23.3)], dtype=student3)
print("student3")
print(a3)

student4 = np.dtype([('name','a20'),('age', 'i1'),('mark','<f4')])
a4 = np.array([('ann', 10, 21.1),('bell', 11, 22.2),('carol', 12, 23.3)], dtype=student1)
print("student4")
print(a4)


"""
student1
[(b'ann', 10, 21.1) (b'bell', 11, 22.2) (b'carol', 12, 23.3)]   //b-byte
student2
[(1, 10, 21.) (2, 11, 22.) (3, 12, 23.)]
student3
[('ann', 10, 21.1) ('bell', 11, 22.2) ('carol', 12, 23.3)]
student4
[(b'ann', 10, 21.1) (b'bell', 11, 22.2) (b'carol', 12, 23.3)]
"""