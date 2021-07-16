# Lista de compresiones

'''
lista = list()
for x in range(4,31,2):
    if x%3 == 0:
        lista.append(x**2)
    
print(lista)
'''

mi_dict = dict()
for x in range(3,11):
    mi_dict[(x,x**3)] = []
    for y in range(4,31,2):
        if y%x == 0:
            mi_dict[(x,x**3)].append(y**2)

print(mi_dict)

# mi_lista = [x**2 for x in range(4,31,2) if x%3 == 0]
# print(mi_lista)

mi_diccionario = { (y,y**3): [x**3 for x in range(4,31,2) if x%y == 0 ] for y in range(3,11) }
print(mi_diccionario)

# print(True if mi_diccionario.values() == mi_dict.values() else False)
# print(mi_diccionario.values())
# print(mi_dict.values())

resultado = all(list(map(lambda x: x[0] == x[1], 
list(zip(mi_dict.values(),mi_diccionario.values())))))
# print(resultado)

# 13824
valor = 13824

resultado = any(list(map(lambda x: valor in x[0] or valor in x[1], 
list(zip(mi_dict.values(),mi_diccionario.values())))))
print(resultado)