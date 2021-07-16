# conversion de cadenas de caracteres

'''
cadena = 'grupo_09'
lista = list(cadena)
print(lista)
'''

'''
cad = 'hola'
cad2 = 'adios'
num = 15
tupla1 = tuple(cad)
tuplaGeneral = tupla1,num,tuple(cad2)
print(tuplaGeneral)
'''

'''
cadena = 'hhola'
print(set(cadena))

cadena_num = '298345328883940'
print(set(cadena_num))

lista = list()
for x in range(len(cadena_num)):
    lista.append(int(cadena_num[x]))

print(set(lista))
'''

# conversión de listas

'''
lista = ['h','o','l','a',1,2,3,('1',2)]
try:
    cadena = ''.join(lista)
    print(cadena)
except:
    print('Error al concatenar variables not string')


lista2 = list()

lista_3 = lista.pop(len(lista)-1)
lista.append(lista_3[0])
lista.append(lista_3[1])

for x in lista:
    lista2.append(str(x))

cadena = ''.join(lista2)
print(cadena)
'''

'''
lista = ['h','o','l','a',123,[1,2],'Grupo_09']
print(lista)
tupla = tuple(lista)
print(tupla)
'''

'''
lista = ['h','o','o','l','a',1,2,3]
conjunto = set(lista)
print(conjunto)
conjunto.add(4)
conjunto.add(5)

print(conjunto)
'''

# conversión de tuplas

'''
tupla = 'h','o','l','a'
cadena = ''.join(tupla)
print(cadena)
'''

'''
tupla = ('hola',12345,'grupo')
lista = list(tupla)
print(lista)
'''

'''
tupla = ('hola',1234,'grupo','hola','Hola')
conjunto = set(tupla)
conjunto.add(555)
print(conjunto)
'''

# Conversión de conjuntos

'''
conjunto = {'h','o','l','a'}
cadena = ''.join(conjunto)
print(cadena)

conjunto2 = {'h'}
conjunto2.add('o')
conjunto2.add('l')
conjunto2.add('a')
print(conjunto2)

conjunto2 = {4,5,2,3,1,2,4,5,7,8,9,6,4,2,3,5,6,7,8,}
print(conjunto2)
'''

'''
conjunto = {'h','o','l','a'}
tupla = tuple(conjunto)
print(tupla)
'''

'''
conjunto = {'h','o','l','a'}
lista = list(conjunto)
print(lista)
'''

# Conversión de diccionarios

'''
cadena = 'grupo_09'

diccionario = dict()
for posicion in range(len(cadena)):
    diccionario[posicion] = cadena[posicion]

print(diccionario)
'''

'''
cadena = 'hola'
diccionario = dict(zip(range(len(cadena)),cadena))
print(diccionario)
'''

'''
lista = ['h','o','l','o']
dict_lista = dict(zip(range(len(lista)),lista))
print(dict_lista)
'''

'''
tupla = 'h','o','l','a'
dict_tupla = dict(zip(range(len(tupla)),tupla))
print(dict_tupla)
'''

'''
conjunto = {'h','o','l','a'}
dict_conjunto = dict(zip(range(len(conjunto)),conjunto))
print(dict_conjunto)
'''

'''
lista = ['h','o','l','a']
diccionario = dict(zip(lista,range(len(lista))))
print(diccionario)
'''

'''
numero = [1,2,3,4,5,6,7]
numero_l = ['uno','dos',('tres',[1,2,3,4]),'cuatro','cinco','seis'] 

diccionario = dict(zip(numero,numero_l))
print(diccionario)
'''

'''
numero = {1,2,3,4,5,6,7}
numero_l = ['uno','dos',('tres',[1,2,3,4]),'cuatro','cinco','seis','siete'] 
diccionario = dict(zip(numero,numero_l))
print(diccionario)
'''

'''
numero = {1,2,3,4,5,6,7}
numero_l = ['uno','dos',('tres',[1,2,3,4]),'cuatro','cinco','seis','siete'] 
letras = ('a','b','c','d','e','f','g')
lista = list(zip(numero,numero_l,letras))
print(lista)
'''

'''
diccionario = {0:'h',1:'o',2:'l',3:'a'}
cadena = ''.join(diccionario.values())
print(cadena)
'''

'''
diccionario = {
    0:'h',
    1:'o',
    2:'l',
    3:'a'
}

tuplaLlave = tuple(diccionario.keys())
tuplaValores = tuple(diccionario.values())
tuplaItems = tuple(diccionario.items())

print(tuplaLlave)
print(tuplaValores)
print(tuplaItems)
'''

'''
diccionario = {
    0:'h',
    1:'o',
    2:'l',
    3:'a'
}

listaLlave = list(diccionario.keys())
listaValores = list(diccionario.values())
listaItems = list(diccionario.items())

print(listaLlave)
print(listaValores)
print(listaItems)

print(diccionario.items())
'''

diccionario = {
    0:'h',
    1:'o',
    2:'l',
    3:'a',
    4:'a'
}
print(diccionario)

conjuntoLlave = set(diccionario.keys())
conjuntoValores = set(diccionario.values())
conjuntoItems = set(diccionario.items())

print(conjuntoLlave)
print(conjuntoValores)
print(conjuntoItems)