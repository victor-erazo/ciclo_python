# leer o escribir en archivo txt

datos = ['linea 1','linea 2','linea 3','linea 4','linea 5']

ruta = r'C:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\ciclo_uno\GRUPO_09\Semana 5\archivo_l.txt'
fichero = open(ruta,'w')

'''
for lie in datos:
    fichero.write(lie)
    fichero.write('\n')   
fichero.close()


for i in range(2001):
    for lie in datos:
        var = str(i) + ', ' + lie
        fichero.write(var)
    fichero.write('\n')
fichero.close()
'''


ruta = r'C:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\ciclo_uno\GRUPO_09\Semana 5\archivo_p.txt'
fichero = open(ruta,'w')

for lie in datos:
    print(lie, file=fichero)
fichero.close()

ruta = r'C:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\ciclo_uno\GRUPO_09\Semana 5\archivo_list_com.txt'
fichero = open(ruta,'w')

fichero.writelines('%s\n' % s for s in datos)
fichero.close()
