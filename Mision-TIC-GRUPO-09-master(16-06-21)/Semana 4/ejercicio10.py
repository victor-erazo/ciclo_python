# Concatenar todos los elementos de la lista.
from functools import reduce

lista = ['python','java','Ruby','Elixir']
result = reduce(lambda acum = '',elem = '':acum + ' - ' + elem,
list(map(lambda ele : ele[0:2],lista)))
print(result)


lista_numero = [1,2,3,4,5,6,7,8,9]
resultado = reduce(lambda acum = 0, elem = 0: acum + elem,lista_numero, 10)
print(resultado)