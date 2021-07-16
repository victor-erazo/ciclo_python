# libreria numpy - crear matrices 

import numpy as np

matriz = np.zeros((4,5))
print(matriz)

matriz = np.ones((3,3))
print(matriz)

c = np.full((5,6),8)
print(c)

matriz_c = np.eye((4))
print(matriz_c)

matriz_ale = np.random.random((3,3))
print(matriz_ale)