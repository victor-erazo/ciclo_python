# libreria pandas - dataFrames, array numpy

import numpy as np
import pandas as pd

unidades_datos = np.array([
    [2,5,3,4],
    [4,6,7,2],
    [3,2,4,1]
])


# print(unidades_datos)
unidades = pd.DataFrame(unidades_datos)
print(unidades)

unidades = pd.DataFrame(unidades_datos, index=['2015','2016','2017'],
                        columns=['Ag','Au','Cu','Pt'])

unidades.index.name = 'Años'
unidades.columns.name = 'Elementos'
print(unidades)



unidades_2015 = {'Ag':2, 'Au':5, 'Cu':3, 'Pt':2}
unidades_2016 = {'Ag':4, 'Au':6, 'Cu':7, 'Pt':2}
unidades_2017 = {'Ag':3, 'Pd':2, 'Cu':4, 'Pt':1}

unidades = pd.DataFrame([unidades_2015,unidades_2016,unidades_2017], index=[2015,2016,2017])
print(unidades)

