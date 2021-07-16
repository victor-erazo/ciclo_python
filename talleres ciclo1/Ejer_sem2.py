#Ejercicios semana dos

#1. Leer un número entero y determinar si es un número terminado en 4.
'''
x = int(input('digite un numero entero...'))

if x == 4:
    print('El numero es cuatro')
elif x % 10 == 4:
    print('El numero termina en cuatro')
else:
    print('El numero no termina en 4')
'''

#2. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
'''
x = int(input('digite un numero entero de dos digitos...'))

if len(str(x)) != 2:
    print('El numero no tiene dos digitos')
elif len(str(x)) == 2:
    x = str(x)
    x1 = x[0]
    x2 = x[1]
    if x1 % 2 == 0 and x2 % 2 == 0:
        print('Ambos digitos son pares')
    else:
        print('Los digitos no son pares')
'''

#5. Leer un número entero de dos dígitos y 
# determinar si es primo y además si es negativo.

#un número primo es un número natural mayor que 1 que tiene
#únicamente dos divisores distintos: él mismo y el 1.
'''
x = int(input('digite un numero entero de dos digitos...'))
if x <= 0:
    print('El numero es negativo')
if len(str(x)) != 2:
    print('El numero no tiene dos digitos')
elif len(str(x)) == 2 and x > 0:
    for i in range(2, x + 1):
        if x % i != 0:
            print(False)
        else: 
            print('Es primo')

'''
#7. Leer dos números enteros y determinar cuál es el mayor.
'''
x = int(input('digite un numero entero ...'))
y = int(input('digite un numero entero ...'))

if x > y:
    print('x es mayor que y')
elif x < y:
    print('x es menor que y')
else:
    print('x e y son iguales')
'''

#9. Leer un número entero de tres dígitos
#  y determinar en qué posición está el mayor dígito.
'''
x = int(input('digite un numero entero de tres digitos ...'))

if x < 0 and x >= -999:
    x *=-1
    print('Negativo de 3 digitos cambiado a positivo')

    len(str(x))
    x = str(x)
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]

    if x1 > x2 and x1 > x3:
        print('El de la primera posicion es el mayor')
    if x2 > x1 and x2 > x3:
        print('El de la segunda posicion es el mayor')
    if x3 > x1 and x3 > x2:
        print('El de la tercera posicion es el mayor')
    if x1 == x2 == x3:
        print('todos los digitos son iguales')

elif x >= 100 and x < 999:

    len(str(x))
    x = str(x)
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]

    if x1 > x2 and x1 > x3:
        print('El de la primera posicion es el mayor')
    if x2 > x1 and x2 > x3:
        print('El de la segunda posicion es el mayor')
    if x3 > x1 and x3 > x2:
        print('El de la tercera posicion es el mayor')
    if x1 == x2 == x3:
        print('todos los digitos son iguales')
    
else:
    print('El numero no tiene tres digitos') 
'''
#11. Leer tres números enteros de dos dígitos cada uno y 
# determinar en cuál de ellos se encuentra el mayor dígito.

'''
def el_mayor_dig(num):
    if num <= -10 and num > -100:
        num *= -1
        num = str(num)
        alfa = num[0]
        beta = num[1]
        if int(alfa) > int(beta):
            return int(alfa)
        elif int(alfa) < int(beta):
            return int(beta)
        else:
            return int(alfa)
    elif num >= 10 and num < 100:
        num = str(num)
        alfa = num[0]
        beta = num[1]
        if int(alfa) > int(beta):
            return int(alfa)
        elif int(alfa) < int(beta):
            return int(beta)
        else:
            return int(alfa)

a, b, c = -17, 74, 11

x1 = el_mayor_dig(a)
x2 = el_mayor_dig(b)
x3 = el_mayor_dig(c)

if x1 > x2 and x1 > x3:
    print('x1 es el mayor')
if x2 > x1 and x2 > x3:
    print('x2 es el mayor')
if x3 > x1 and x3 > x2:
    print('x3 es el mayor')
if x1 == x2 == x3:
    print('todos los digitos son iguales')
if x1 > x3 and x2 > x3 and x1 == x2:
    print('x1 o x2 es el mayor')
if x2 > x1 and x3 > x1 and x2 == x3:
    print('x2 o x3 es el mayor')
if x3 > x2 and x1 > x2 and x3 == x1:
    print('x1 o x3 es el mayor')
'''
#13. Leer un número entero menor que 50 
# y positivo y determinar si es un número primo.
'''
x = 23

if x >=2 and x < 50:
    print('positivo menor de 50')
    for i in range(2, x + 1):
        if x % i != 0:
            print(i,False)
        else: 
            print('Es primo')
else:
    print('No esta entre 0 y 50')
'''
#15. Leer un número entero y determinar si es múltiplo de 7.
'''
y = 70

if y % 7 == 0:
    print('es multiplo de siete')
else:
    print('No es multiplo de siete')
'''
# 17. Leer un número entero de 4 dígitos y 
# determinar si tiene mas dígitos pares o impares.
'''
num = 2759

lista = []

if num >= 1000 and num < 10000:
    num = str(num)
    for ind in num:
        lista.append(int(ind))
else:
    print('El No esta por fuera del rango')

print(lista)

for x in range(len(lista)):
    if lista[x] % 2 == 0:
        print('El elemento en la posicion No' , x+1, "es par")
    else:    
        print('El elemento en la posicion No', x+1, "es impar")
'''
#19. A un trabajador le pagan según sus horas trabajadas por una 
# tarifa de pago por hora. Si la cantidad de horas trabajadas es 
# mayor 40 horas. La tarifa se incrementa en un 50% para las horas 
# extras. Calcular el salario del trabajador dadas las horas trabajadas 
# y la tarifa ingresadas por el usuario.
'''
horas_trab = 45
vlr_hora = 10000

def salario(horas,valor):

    if horas >= 40:
        horas_ext = horas - 40
        valor_ext = valor*(.5)
        salario = horas*valor + horas_ext*valor_ext
        return salario
    else:
        salario = horas * valor
        return salario

print('El salario del trabajador es: $',salario(horas_trab,vlr_hora))
'''
#21. Hacer un programa que pida al usuario las tres notas de un alumno
# (deben estar entre 0 y 5 y pueden tener decimales) y 
# calcule el promedio e indique mediante un mensaje si aprobó o no
# (aprueba con nota mayor a 3). 
# Se debe validar que las notas introducidas estén dentro del rango permitido.
'''
def prom_notas():
    nota = 0
    suma = 0
    contar = 0

    while contar < 3:
        nota = int(input('Ingrese la nota No:{} '.format(contar+1)))
        suma += nota
        contar += 1

    promedio = suma/contar
    return promedio

print('El promedio del estudiante es:',round(prom_notas(),2))
'''












      




       












