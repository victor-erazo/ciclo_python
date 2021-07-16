padres = list()
hijos = list()

for x in range(3):
    pa = input('Ingrese el nombre del padre : ')
    ma = input('Ingrese el nombre de la madre : ')
    padres.append([pa,ma])
    cantidad_hijos = int(input('Ingrese el numero de hijos : '))
    hijos.append([])
    for k in range(cantidad_hijos):
        hi = input('Ingrese el nombre del hijo : ')
        hijos[x].append(hi)
    
print(padres)
print(hijos)

print('El nombre de los padre, madre y sus hijos')
for x in range(len(padres)):
    print("Padre : ", padres[x][0])
    print("Madre : ", padres[x][1])
    for k in range(len(hijos[x])):
        print("hijo :", hijos[x][k])

print('El nombre de padre y cantidad de hijos')
for j in range(len(padres)):
    print("Padre : ",padres[j][0])
    print("Numero de hijos : ", len(hijos[j]))