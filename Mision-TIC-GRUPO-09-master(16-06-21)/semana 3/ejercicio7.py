notas = [8,7,9]
alturas = [1.56,1.76, 1.80]
dias = ['lunes', 'martes','miercoles']

# tres elementos de tipo lista dentro de una lista
notas_l = [[4,5],[6,9],[8,7]] 

lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(lista)
# print(lista[0])
# print(lista[0][0])

'''
for x in range(len(lista[0])):
    print(lista[0][x])
'''

'''
for k in range(len(lista)):
    for j in range(len(lista[k])):
            print(lista[k][j])
'''

lista2 = [[2,3,4,8,1],[4,9,7,8,2]]

'''
for k in range(len(lista2)):
    result = 0
    for j in range(len(lista2[k])):
        result = result + lista2[k][j]
    print(result)


for k in range(len(lista2)):
    result = 0
    result = sum(lista2[k])
    print(result)
'''

result = 0
for k in range(len(lista2)):
    for j in range(len(lista2[k])):
        result = result + lista2[k][j]

print(result)