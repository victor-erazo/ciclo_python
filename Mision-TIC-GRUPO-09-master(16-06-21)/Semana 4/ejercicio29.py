# Libreria pandas - dataFrames
from numpy import index_exp
import pandas as pd


datos = {'manzanas': [3,2,0,1], 'naranjas':[0,7,2,4]}

compras = pd.DataFrame(datos, index = ['Juan','Roberto','Lili', 'Maria'])

# print(compras.index)
# print(compras.columns)

compras.index.name = 'Clientes'
compras.columns.name = 'Frutas'

print(compras)

print(compras.axes)


