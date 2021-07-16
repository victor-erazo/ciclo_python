# Libreria numpy - indexación de matrices - rebanar

import numpy as np

'''
a = np.array([
    [1,2,3],
    ['a','b','c']
])

print(a)
'''

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(a)

b = a[0:2,1:3]
print(b)

'''
c = a[0:1,2:3]
print(c)
d = a[1:3,:2]
print(d)
'''

# print(np.fliplr(a))

b[0,0] = 77
a[1,2] = 100

print(a)
print(b)
