# libreria pandas - dataFrames

import pandas as pd

elementos = {
    'Numero atómico': [1,6, 47, 88],
    'Masa atómica': [1.008, 12.011, 107.87,226],
    'Familia':['No metal','No metal','Metal','Metal']
}

# print(elementos)

tabla_periodica = pd.DataFrame(elementos)
print(tabla_periodica)

tabla_periodica = pd.DataFrame(elementos, index=['H','C','Ag','Ra'],
                    columns=['Familia','Numero atómico','Masa atómica'])

print(tabla_periodica)