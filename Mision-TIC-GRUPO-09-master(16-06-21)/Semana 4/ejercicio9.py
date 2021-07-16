# Funcion reduce
# Obtener la suma de todos los elementos de una lista

from functools import reduce

'''
lista = [1,2,3,4,5,6,7,8,9]
acumulador = 0

for ele in lista:
    acumulador += ele

print(acumulador)
'''

lista = [1,2,3,4,5,6,7,8,9]

def funcion_acumular(acum = 0,elem = 0):
    return acum + elem

resultado = reduce(funcion_acumular,lista)
print(resultado)

resultado_lambda = reduce(lambda acum = 0, elem = 0: acum + elem,lista)
print(resultado_lambda)