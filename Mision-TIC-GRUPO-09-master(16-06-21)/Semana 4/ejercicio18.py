# Libreria numpy - rango mas bajo y matriz general

import numpy as np

a = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print(a)

row_r1 = a[1,:]
row_r2 = a[1:2,:]

print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)

print(row_r1[2])
print(row_r2[0,2])

col_c1 = a[:,1]
col_c2 = a[:,1:2]

print(col_c1, col_c1.shape)
print(col_c2, col_c2.shape)

print(col_c2[0,:1])