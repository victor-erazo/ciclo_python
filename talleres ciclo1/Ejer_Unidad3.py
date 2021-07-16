#Ejercicios unidad 3 'Pares'

#2. Se ingresan un conjunto de n alturas de personas por teclado.
#  Mostrar la altura promedio de las personas.
'''
n = 5
contar = 0
suma = 0
altura = []

while n > 0:

    altura.append(int(input('ingrese altura en cm: '))) 
    n -= 1
    contar += 1

prom = sum(altura)/contar
print(f'La altura promedio es {prom} cms')
'''

#4. Realizar un programa que imprima 25 términos de la 
# serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)
'''
for x in range(11,45,11):
    print(x, end = ' ')
'''
'''
num = 11
delta = 11
while num < 45:
    print(num, end = ' ')
    num += delta
'''

#6. Realizar un programa que permita cargar dos listas de 15 valores cada una. 
# Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
'''
lista_1 = []
lista_2 = [] 

def acum_listas():
    n, n1, n2, suma_1, suma_2 = 0,0,0,0,0
        
    while n < 16: #cambiarlo a 4 para probar
        
        n1 = int(input('lista 1: digite un entero entre 1 y 10 '))
        n2 = int(input('lista 2: digite un entero entre 1 y 10 '))

        lista_1.append(n1)
        lista_1.append(n2)
        n += 1

    suma_1 = sum(lista_1)
    suma_2 = sum(lista_2)

    if suma_1 > suma_2:
        return 'La lista 1 es mayor'
    elif suma_1 < suma_2:
        return 'La lista 2 es mayor'
    else:
        return 'Listas iguales'

print(lista_1, suma_1)
print()
print(lista_2, suma_2)
print(acum_listas())
'''
# 8. Confeccionar un programa que lea n pares de datos, cada par de datos 
# corresponde a la medida de la base y la altura de un triángulo.
#  El programa deberá informar: 
# a) De cada triángulo la medida de su base, su altura y su superficie. 
# b) La cantidad de triángulos cuya superficie es mayor a 12.
'''
n = 2
base = list()
altura =list()
area = []
dato_b, dato_a, dato_area = 0,0,0

for x in range(0,n):

    dato_b =int(input('Ingrese un No entero positivo para la base: '))
    dato_a =int(input('Ingrese un No entero positivo para la altura: '))
    dato_area = dato_b * dato_a / 2

    base.append(dato_b)
    altura.append(dato_a)
    area.append(dato_area) # 

    print(f'El triangulo No {x + 1} de area {dato_area}, base {dato_b} y altura {dato_a}\n')
    
    if dato_area > 12:
        print(f'El triangulo No {x + 1} tiene un area mayor a 12\n')
'''
# 10. Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)

#resultado = 0
'''
for x in range(5,51):
    resultado = 5 * x
    print(f'5 x {x} = {resultado}')
'''
#12. Realizar un programa que lea los lados de n triángulos, e informar:
#  a) De cada uno de ellos, qué tipo de triángulo es: 
#  equilátero (tres lados iguales), isósceles (dos lados iguales), 
#  o escaleno (ningún lado igual) 
#  b) Cantidad de triángulos de cada tipo.


'''
triangulos = {'triangulo_1': {'lado_1':5,'lado_2':5,'lado_3':2,},
              'triangulo_2': {'lado_1':5,'lado_2':4,'lado_3':3,},
              'triangulo_3': {'lado_1':6,'lado_2':6,'lado_3':6,}}

print(triangulos.keys())
print(triangulos.values())

print(triangulos.items())
print()


tri_equi, tri_esc, tri_iso = 0,0,0
for x in triangulos.values():

    if x['lado_1']==x['lado_2']==x['lado_3']:
        print(f'El triangulo {x} es equilatero')
        tri_equi += 1
    elif x['lado_1'] == x['lado_2'] or x['lado_1']==x['lado_3'] or x['lado_2']==x['lado_3']:
        print(f'El triangulo {x} es isoceles')
        tri_iso += 1
    else:
        print(f'El triangulo {x} es escaleno')
        tri_esc += 1
print()
print(f'La cantidad de triangulos de cada tipo:\nisoceles: {tri_iso}\nescaleno: {tri_esc}\nequilatero: {tri_equi}')
'''
#14 Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos. 
# b) La cantidad de valores ingresados positivos. 
# c) La cantidad de múltiplos de 15. 
# d) El valor acumulado de los números ingresados que son pares.
'''
num = 0
positivos = list()
negativos = list()
multi_15 = list()
pares = list()
contar_pos = contar_neg = contar_15 = 0

for x in range(1,11):

    num = int(input('Ingrese un No entero (positivo o negativo): '))

    if num >= 0:
        positivos.append(num)
        contar_pos += 1
    if num < 0:
        negativos.append(num)
        contar_neg += 1
    if num % 15 == 0:
        multi_15.append(num)
        contar_15 += 1
    if num % 2 == 0:
        pares.append(num)

print('termino\n')
print(positivos)
print(negativos)
print(multi_15)
print(pares,'\n')
suma_pares = sum(pares)
print(f'Positivos: {contar_pos}\nNegativos: {contar_neg}\nMultiplos de 15: {contar_15}\nSuma de pares: {suma_pares}')

'''
# 16. Cargar una oración por teclado. Mostrar luego cuantos espacios
#  en blanco se ingresaron. Tener en cuenta que un espacio en blanco
#  es igual a " ", en cambio una cadena vacía es ""

'''
texto = 'Este grupo 09 de programacion es una chimba (muy bueno)!'
esp_blanco = texto.count(' ')
print('El No de espacios en blanco es',esp_blanco)
'''

# 18. Solicitar el ingreso de una clave por teclado y almacenarla 
# en una cadena de caracteres. Controlar que el string ingresado 
# tenga entre 10 y 20 caracteres para que sea válido, 
# en caso contrario mostrar un mensaje de error.
'''
clave = input("Ingrese una contrasena entre 10 y 20 caracteres(numeros o letras):\n")

if len(clave) >= 10 and len(clave) <= 20:
    print('Contrasena asignada con exito')
else:
    print('La contrasena no tiene entre 10 y 20 caracteres')

print(clave)
'''

'''
itinerario = [['Santa Marta',1],['Cartagena', 2],['San Andres', 4]]
print(itinerario[0])
print(itinerario[0][0])
print(itinerario[0][1])
itinerario[0][1] = 2
print(itinerario[0])
#cambiar la posicion de santa marta y san andres:
itinerario[0],itinerario[2] = itinerario[2],itinerario[0]
print(itinerario)
'''

'''
itinerario = [['Santa Marta',1],['Cartagena', 2],['San Andres', 4]]

for x,y in itinerario:
    print('Destino:', x)
    print('No de dias:',y)
'''











    







 







