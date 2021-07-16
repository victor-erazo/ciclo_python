# exportar diccionario ha archivos json

import json

datos = dict()

datos['clientes'] = []

datos['clientes'].append(
    {
        'pr_nombre':'Sigrid',
        'sg_nombre': 'Mannock',
        'edad': 27,
        'salario': 7.17
    }
)

datos['clientes'].append(
    {
        'pr_nombre':'Joe',
        'sg_nombre': 'Hinners',
        'edad': 31,
        'salario': [1.90, 5.50]
    }
)

datos['clientes'].append(
    {
        'pr_nombre':'Theodoric',
        'sg_nombre': 'Rivers',
        'edad': 36,
        'salario': 1.11
    }
)

ruta = r'C:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\ciclo_uno\GRUPO_09\Semana 5\archivo.json'

with open(ruta,'w') as file:
    json.dump(datos,file, indent=4)