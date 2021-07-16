'''
  contador = contador + 1
  contador += 1

  acumulador = acumulador + variable
  acumulador += variable

'''

'''
lista = [1, 2.5,'DevCode',[7,9],4]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[3][0])
print(lista[3][1])
print('hacemos un cambio -> ', lista[1:4])

print(lista[0:5])
print(lista[1:6:2])
print(lista[1:6:4])
'''

'''
lista = []
print(lista)
nombre = 'Juan'
edad = 29
lista = [nombre,edad]
print(lista)
nombre = 'Rafael'
print(lista)
'''

'''
nombres = ['Ana', 'Bernardo']
edades = [26,31]
lista = [nombres,edades]
print(lista)

nombres += ['Catalina']
nombres[0] = 'Jorge'

print(lista)
'''

'''
factura = ['pan','huevo',200,350]

print(factura[0])
print(factura[3])
print(factura[-len(factura)])
print(factura[-3])
'''

version_phone = [6,7,8,13]
# print(version_phone)
version_phone.append(10)
# print(version_phone)
version_phone.append('iphone_12')
# print(version_phone)
# print(version_phone.count('iphone_12'))

version_phone.extend([2.5])
# print(version_phone)
version_phone.extend(range(13,17))
# print(version_phone)

'''
try:
    print(version_phone.index(1))
except:
    print('el valor no se encuentra en la lista')
'''

'''
version_phone.pop()

version_phone.insert(2,3.6)
print(version_phone)

version_phone.pop(6)
print(version_phone)

# version_phone.remove(13)
# print(version_phone)
version_phone.reverse()
print(version_phone)

version_phone.sort()
print(version_phone)

# boo_t= True
version_phone.sort(reverse=True)
print(version_phone)
'''

lista = [2,'cms',True,['phone',10]]

l2 = lista[1]

print(l2)
