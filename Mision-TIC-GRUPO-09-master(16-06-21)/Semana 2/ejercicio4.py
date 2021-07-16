'''
{} llaves
[] corchetes
() parentesis
'''

'''
diccionarioUno = {"total": 55,"descuento": True,15:"15"}
print(diccionarioUno)
diccionarioDos = {"nombre": 5 *3,"telefono":3215555555,"edad": 28, "ciudad":"pereira"}
print(diccionarioDos)

diccionarioTres = {"total": 55, 10: "curso de python",2.0: True}
print(diccionarioTres)
print(diccionarioTres[10])
'''


'''
usuario = {
    "nombre":"Juan",
    "edad": 24,
    "curso": "curso de python",
    "habilidad": {
        "programacion": True,
        "base_de_datos": False
    },
    "no medallas": 12
}

print(usuario)
print(usuario['curso'])
print(usuario['habilidad'])
print(usuario['habilidad']['base_de_datos'])

usuario['habilidad']['SQL'] = True
print(usuario)


diccionario = dict(total = 55, descuento = True, subtotal = "15")
print(diccionario)
'''

diccionario = dict()
print(diccionario)

diccionario['marca'] = "Mazda"
print(diccionario)
diccionario['marca'] = "Subaru"
print(diccionario)

diccionario = {"Fernando":1,"Juan":2,"Marcos":3,"Jorge":4}
print(diccionario.keys())
print(diccionario.values())

# diccionario.clear()
# print(diccionario)

copiaDiccionario = diccionario.copy()
print(copiaDiccionario)

secuencia = ('python','zope','plone')
nuevo_diccionario = dict.fromkeys(secuencia," ")
print(nuevo_diccionario)
