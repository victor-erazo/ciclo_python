# x = x + 1

'''
n = 5
while n > 0:
    print(n)
    n = n - 1

print('Termino!')
'''

'''
# retorno de la función es un entero
def factorial(n : int)-> int:
    resultado = 1
    n_actual = 2
    while n_actual <= n:
        resultado = resultado * n_actual
        n_actual += 1
    return resultado

print(factorial(10))
'''

'''
def factorial(n : int)-> int:
    resultado = 1
    n_actual = 2
    while not n_actual > n:
        resultado = resultado * n_actual
        n_actual += 1
    return resultado

print(factorial(10))
'''

'''
i = 1
while i > 0:
    print(i)
    i += 1
print('Terminar')
'''

'''
i = 1
while i != 10:
    print(i)
    i += 2
print('Terminar')
'''


'''
i = 100
while i > 0:
    # print(i)
    i = i - 1
print('Termino')
'''

'''
promedio, total, contar = 0.0, 0, 0
print('Introduzca la nota del estudiante (-1 para salir)')
nota = int(input())
while nota != -1:
    total = total + nota
    contar = contar + 1
    print('Introduzca la nota del estudiante (-1 para salir)')
    nota = int(input())

promedio = total / contar
print('La nota promedio de los estudiantes es : ', promedio)
'''

'''
promedio, total, contar = 0.0, 0, -1
nota = 0
while nota != -1:  
    total = total + nota
    contar = contar + 1
    print('Introduzca la nota del estudiante (-1 para salir)')
    nota = int(input())
    
promedio = total / contar
print('La nota promedio de los estudiantes es : ', promedio)
'''

'''
promedio, total, contar = 0.0, 0, -1
nota = 0
while nota != -1:  
    total = total + nota
    contar = contar + 1
    print('Introduzca la nota del estudiante (-1 para salir)')
    nota = int(input())
else:    
    promedio = total / contar
    print('La nota promedio de los estudiantes es : ', promedio)
'''

'''
x = 1
if x == 2:
    print(x)
else:
    print(x)
'''

'''
variable = 10

while variable > 0:
    print('El numero actual es : ', variable)
    variable = variable - 1
    if variable == 5:
        break
'''
'''
variable = 10
x = 0 
while variable > 0:
    variable = variable - 1
    x = x + 1
    if variable == 5:
        variable -= 1
        continue
        
    print('El numero actual es : ', variable)
    # print('valor ', x)
'''