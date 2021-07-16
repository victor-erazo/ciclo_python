diccionarioEstudiantes = {
    'E3454fdf':{
        'nombres': 'Laura',
        'apellidos': 'Jaramillo',
        'acudientes':[
            {
                'acudiente_uno': 'Andrea',
                'acudiente_dos': 'Juan'
            }
        ],
        'promedio': 5.0
    },
    'Egg56dfg':{
        'nombres': 'Samir',
        'apellidos': 'Gómez',
        'acudientes': [
            {
                'acudiente_uno': 'Alejandro',
                'acudiente_dos': 'Sofía'
            }
        ],
        'promedio': 4.0
    },
    'FHT43523': {
        'nombres': 'Iván',
        'apellidos': 'Arcila',
        'acudientes': [
            {
                'acudiente_uno': 'Esposa',
                'acudiente_dos': ''
            }
        ],
        'promedio': 5.0
    },
    'Z4edkdf':{
        'nombres': 'Sara',
        'apellidos': 'Cabrera',
        'acudientes': [
            {
                'acudiente_uno': 'Ricardo',
                'acudiente_dos': 'Luz Stella'
            },
            {
                'acudiente_uno': 'Fran',
                'acudiente_dos': 'Carmen'
            },
            {
                'acudiente_uno': 'Maria',
                'acudiente_dos': 'Angy'
            }
        ],
        'promedio': 3.5
    }
}

'''
print(diccionarioEstudiantes)
print(diccionarioEstudiantes.keys())
print(diccionarioEstudiantes.values())
print(diccionarioEstudiantes.items())
'''

'''
for llave in diccionarioEstudiantes:
    print(llave)
'''

'''
for codigoEstudiante,infoEstudiande in diccionarioEstudiantes.items():
    print('Codigo: ', codigoEstudiante)
    print('Información: ', infoEstudiande)
'''

# Obtener todos los acudientes del diccionarioEstudiantes

'''
for acudientes in diccionarioEstudiantes.values():
    print(acudientes.get('acudientes'))
'''

# Obtener todos los acudientes dos del dicionarioEstudiantes

'''
for acudientes in diccionarioEstudiantes.values():
    print(acudientes.get('acudientes')[0]['acudiente_dos'])
'''

'''
for codigoEstudiante,infoEstudiantes in diccionarioEstudiantes.items():
    print(infoEstudiantes['acudientes'][0]['acudiente_dos'])
'''

'''
for codigoEstudiante,infoEstudiantes in diccionarioEstudiantes.items():
    for acu in range(len(infoEstudiantes['acudientes'])):
        print(infoEstudiantes['acudientes'][acu]['acudiente_dos'])
'''

# Obtener los nombres y apellidos que obtuvieron nota mayor a 4 
# eliminar los demas estudiantes del dict 

for codigoEstudiante,infoEstudiante in diccionarioEstudiantes.items():
    promedio = infoEstudiante['promedio']
    if promedio > 4:
        print('Estudiante : ' + infoEstudiante['nombres']+ ' '+infoEstudiante['apellidos'])
    else:
        # del diccionarioEstudiantes[codigoEstudiante]
        diccionarioEstudiantes.pop(codigoEstudiante)
