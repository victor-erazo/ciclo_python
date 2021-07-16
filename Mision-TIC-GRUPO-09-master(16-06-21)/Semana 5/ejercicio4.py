# libreria pandas - excel

import pandas as pd

ruta = r'C:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\ciclo_uno\GRUPO_09\Semana 5\archivo.xlsx'

df = pd.read_excel(ruta, sheet_name='personas')
# print(df)

df = pd.read_excel(ruta, sheet_name='personas',header=None, skiprows=1)
# print(df)

df = pd.read_excel(ruta, sheet_name='personas',skiprows=1,
                    names=['Id','Pr Nombre','Sg Nombre','Edad','Salario 1','Salario 2'])
print(df)