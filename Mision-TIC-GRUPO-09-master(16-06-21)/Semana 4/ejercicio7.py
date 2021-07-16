# Funcion filter
# Obtener los elementos de tupla mayores a cinco

def mayor_a_cinco(elemento = 0):
    return elemento > 5

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)

result = set(filter(mayor_a_cinco,tupla))
print(len(result))
print(result)

'''
conjunto = {5,2,6,7,8,10,77,55,2,1,30,4,2,3}
print(conjunto)
'''

result_lambda = tuple(filter(lambda elemento : elemento > 5, tupla))