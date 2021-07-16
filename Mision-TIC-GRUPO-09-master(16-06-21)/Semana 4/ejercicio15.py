# Libreria numpy

import numpy as np

a = np.array([34, 25, 7])

print(type(a))
print(a)
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 45
print(a)

b = np.array([
    [1,2,3],
    [4,5,6]
])

print(b)
print(b.shape)

print(b[0,0], b[0,1], b[1,2])