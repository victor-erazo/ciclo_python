# Funcion map con dos o mas listas

from math import pow

print( pow(2,3) )

numeros = [2,3,4]
potencia = [4,3,2]

resultado = list(map(pow,numeros,potencia))
print(resultado)

'''
def funPotencia(base, exp):
    return base ** exp

resultado = list(map(funPotencia,numeros,potencia))
print(resultado)
'''