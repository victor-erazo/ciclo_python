# Funcion filter

'''
pares = list()
for x in range(11):
    if x % 2 == 0:
        pares.append(x)

print(pares)  
'''

items = [0,1,2,3,4,5,6,7,8,9,10]
resultado = tuple(filter(lambda ele: ele % 2 == 0, items))
print(resultado)