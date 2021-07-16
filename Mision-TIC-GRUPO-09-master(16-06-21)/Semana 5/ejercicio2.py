# libreria pandas

import pandas as pd

ruta = r'C:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\ciclo_uno\GRUPO_09\Semana 5\archivo.csv'

df = pd.read_csv(ruta, sep= ';')
# print(df)

df = pd.read_csv(ruta, sep= ';', header = None)
# print(df)

df = pd.read_csv(ruta, sep= ';', skiprows=1,
            names=['Id','Pr Nombre','Sg Nombre','Edad','Salario 1','Salario 2'])
# print(df)
# print(df['Edad'][4])

df = pd.read_csv(ruta, sep= ';', skiprows=1,
            names=['Id','Pr Nombre','Sg Nombre','Edad','Salario 1','Salario 2'],
            na_values='?')
# print(df)

df = pd.read_csv(ruta, sep= ';', skiprows=1,
            names=['Id','Pr Nombre','Sg Nombre','Edad','Salario 1','Salario 2'],
            na_values='?', index_col='Id')
# print(df)

df = pd.read_csv(ruta, sep= ';', skiprows=1,
            names=['Id','Pr Nombre','Sg Nombre','Edad','Salario 1','Salario 2'],
            na_values='?', index_col=['Pr Nombre','Sg Nombre'])
print(df)
