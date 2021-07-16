'''
for x in range(0,10):
    print('Valor de x : ', x)
'''

'''
for j in range(0,10,2):
    print('La iteracion j : '+ str(j))
'''

'''
for k in range(10,0,-1):
    print('La iteracion decremental k es : ' + str(k))
'''

'''
oracion = 'Mary entiende muy bien python'
frases = oracion.split()
print('la oracion analizar es : ',oracion,'\n')

for palabra in range(len(frases)):
    print('palabra : {} en la posicion es : {}'.format(frases[palabra],palabra))
'''

'''
oracion = 'Mary entiende muy bien python'
frases = oracion.split()
print('la oracion analizar es : ',oracion,'\n')

for palabra in frases:
    print('palabra : {}'.format(palabra))
'''

'''
midic = dict() # midic = {}
lista = list() # lista = []

datos_basicos = {
    'nombres': 'Leonardo Jose',
    'apellidos': 'Caballero Garcia',
    'cedula': '11009321212',
    'fecha_nacimiento': '13-12-1980',
    'lugar_nacimiento': 'Bucaramanga',
    'nacionalidad': 'Colombiano',
    'estado_civil': 'Soltero'
}

print(datos_basicos)

clave = datos_basicos.keys()
# print(clave)
valor = datos_basicos.values()
# print(valor)
cantidad_datos = datos_basicos.items()
print(cantidad_datos,'\n')
'''  


'''
for clave_1 in clave:
    print(clave_1)
for valor_1 in valor:
    print(valor_1)
'''

'''
for cla, val in cantidad_datos:
    print(cla,' : ', val)

for datos in cantidad_datos:
    print(datos)
'''

'''
frutas = {
    'fresa': 'roja', 
    'limon': 'verde',
    'papaya': ' naranja',
    'manzana': 'amarilla',
    'guayaba': 'rosa'
}

for llave in frutas:
    print(llave, ' es el color ', frutas[llave])
'''

db_connection = "127.0.0.1","5432","root","nomina"

for parametros in db_connection:
    print(parametros)
else:
    print("el comando de postgreSQL es : -h=",db_connection[0],' -p=',db_connection[1],
    ' -u=',db_connection[2],' -d=',db_connection[3])