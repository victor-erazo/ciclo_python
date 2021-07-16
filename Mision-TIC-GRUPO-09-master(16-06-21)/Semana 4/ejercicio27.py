# libreria numpy - broadcasting

import numpy as np
from numpy.core.numeric import empty_like

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])
print(a)

b = np.array([1,0,1])

c = np.empty_like(a)
# print(c)

for i in range(4):
    c[i, :] = a[i,:] + b

print(c)