# libreia pandas - dataFrames head

import pandas as pd

entradas = pd.Series([11,18,12,16,9,16,22,28,31,29,30,12],
            index=['Ene','Feb','Mar','Abr','May','Jun',
                    'Jul','Ago','Sep','Oct','Nov','Dic'])

salidas = pd.Series([9,26,18,15,6,22,19,25,34,22,21,14],
            index=['Ene','Feb','Mar','Abr','May','Jun',
                    'Jul','Ago','Sep','Oct','Nov','Dic'])

almacen = pd.DataFrame({"entradas":entradas, "salidas": salidas})
almacen['neto'] = almacen.entradas - almacen.salidas

print(almacen)
