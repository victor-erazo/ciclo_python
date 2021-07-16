'''
fruta = 'fresa'
letra = fruta[1]
print(letra)
letra = fruta[0]
print(letra)

letra = fruta[2.5]
'''


'''
fruta = 'banana'
longitud = len(fruta) -1
print(longitud)

letra = fruta[longitud]
print(letra)

s = 'Monty Python'
print(s[3:7])
print(s[4:8])
print(s[3:9])
print(s[3:8])
'''
'''
fruta = 'banana'
print(fruta[:4])
print(fruta[4:])
print(fruta[3:3])
'''

'''
saludo = 'Buenos dias'
# saludo[0] = 'J'

nuevo_saludo = 'J' + saludo[1:]
print(nuevo_saludo)

print('a' in 'banana')
print('jan' in 'banana')


palabra = 'fresa'

if palabra < 'banana':
    print('la palabra : ', palabra, ' es menor a banana')
elif palabra > 'banana':
    print('la palabra : ', palabra, ' es mayor a banana')
else:
    print('palabras son iguales')

'''

saludo = 'buenos dias'
# print(dir(saludo))
'''
nuevo_saludo = saludo.upper()
print(nuevo_saludo)

index = saludo.find('a')
print(index)
print(saludo[index])

index = saludo.find('di')
print(index)

index = saludo.find('nos',4)
print(index)

linea = '       Aquí estamos          '
print(linea)
print(linea.strip())


linea = 'Que tengas un buen día'
print(linea.startswith('que'))
print(linea.lower().startswith('que'))



camellos = 42

print('%d' % camellos)
print('he visto %d camellos' % camellos)

print('buenos\ndias')
print(r'buenos\ndias')

'''

cadena = 'un uno, un dos, un tres'
print(cadena.replace('un ','XXX '))

