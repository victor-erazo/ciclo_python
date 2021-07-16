# libreira numpy - rebanar matrices

import numpy as np

'''
a = np.array([[1,2], [3,4]])
print(a.shape)
# a[0,0] = 'a'
print(a)
b = np.array([[a,a]])
print(b)
'''

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(a[0,1])
b = a[:2, 1:3]
b[0,0] = 777
print(b)
print(a[0,1])


'''
c = a[1:2, 2:3]
print(c)
d = a[1:3, :2]
print(d)
e = a[0:3, 2:3]
print(e)
'''
# print(np.fliplr(a))