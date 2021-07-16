# libreria pandas - Series

import pandas as pd

s = pd.Series([7,5,6])
# print(s)

s = pd.Series([7,5,6], index=['Ene','Feb','Mar'])
# print(s)


# Utilizando diccionario
d = {'Ene': 7, 'Feb': 5, 'Mar': 6}
s = pd.Series(d)
# print(s)

s = pd.Series(d, index=['Abr','Mar','Feb','Ene'], dtype=int)
#print(s)

# Utilizando un escalar en la serie

s = pd.Series(9, index=['Ene','Feb','Mar','Abr','May'])
print(s)