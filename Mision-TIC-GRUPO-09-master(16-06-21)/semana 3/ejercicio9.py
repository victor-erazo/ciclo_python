'''
cadena = 'Este es un atributo '
cadenaNueva = cadena + 'nuevo'
print('Flujo : ', cadenaNueva)
print(cadenaNueva[0:4])
'''

# distancias = (('pereira','bogota',230),('pereira','cali',260))
# print(distancias)

itinerario = [['Santa Marta',1],['Cartagena',2],['San Andrés',4]]
itinerario.append(['Providencia',2])
itinerario.pop(1)
itinerario[0][1] += 1
itinerario[0],itinerario[-1] = itinerario[-1],itinerario[0]
# itinerario[-1] = itinerario[0]
print(itinerario)

'''
for posicion, valor in enumerate(itinerario):
    print('posicion: ', posicion)
    print('valor', valor[0])
'''

for iti in range(len(itinerario)):
    print('posicion: ', iti)
    print('valor: ', itinerario[iti])



