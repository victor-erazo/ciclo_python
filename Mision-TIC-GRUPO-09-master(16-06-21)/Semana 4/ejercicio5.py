# Funciones map
# Obtener el cuadrado de cada elemento de la lista.

'''
def cuadrado(elemento = 0):
    return elemento * elemento

lista = [1,2,3,4,5,6,7,8,9]

resultado = list( map(cuadrado,lista) )
print(resultado)

resultado = list( map( lambda elemento: elemento * elemento,lista ) )
print(resultado)
'''

# Obtener el factorial de cada elemento de la lista.

lista = [1,2,3,4,5,6,7,8,9]

def factorial(elemento = 0):
    contar = 2
    resultado = 1
    while contar <= elemento:
        resultado = resultado * contar
        contar += 1
    return resultado

resultado = list(map(factorial,lista))
print(resultado)