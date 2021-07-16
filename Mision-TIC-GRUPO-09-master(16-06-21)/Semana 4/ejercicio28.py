# libreria pandas - Series

import pandas as pd

ventas = pd.Series([23,14,35], index=['Ene','Feb','Mar'])
# print(ventas)

# print(ventas[0])
# print(ventas['Ene'])
# print(ventas.dtype)

#print(ventas.index)
#print(ventas.values)

ventas.name = 'Ventas 2021'
ventas.index.name = 'Meses'
# print(ventas)
print(ventas.axes)

