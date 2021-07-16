''''
P : tiene almenos 3.00 en el promedio de la nota
Q : asistio al 80% de las clases
'''
# (P ^ Q)

'''
P : Gana menos de dos salarios minimos
Q : Vive en el sitio de trabajo
R : La empresa suministra transporte completo
S : No se vive cerca del lugar de trabajo (mas de 1000 metros)
'''

# (P ^ Q) ^ (R ^ -S)

# (P ^ S) ^ (-Q ^ -R)

# (-P ^ -R) ^ (S ^ Q)

# (P v Q) v (Q v S)

# (P ^ S) ^ (-R v -Q)

# S ^ (P ^ -Q ^ -R)

# P ^ -(Q ^ R ^ S)

'''
Un año bisiesto es todo año divisible por 4, 
que no es divisible por 100,
de lo contrario debe ser divisible por 400.

P : el anho es divisible por 4
Q : el aho es divisible por 100
R : el anho es divisible por 400

'''

# -(P ^ Q ^ R) 

# P ^ (-Q ^ R)
# P v -Q ^ R
# (R ^ P)
# P ^ (Q v -R) 
# P v (-Q ^ R)

if 1 < 2:
    #print('respuesta correcta')
    pass

'''
horaDeldia = 11

if horaDeldia >= 12:
    horaDeldia = horaDeldia - 12
    print(horaDeldia," p.m.")
else:
    print(horaDeldia," a.m.")
'''
'''
resultadoDelexamen = 90
if resultadoDelexamen > 65:
    print('aprobo el examen')

if resultadoDelexamen >= 90:
    print('excelente trabajo')

numero = 78

if numero > 0:
    print('es positivo')
if numero < 0:
    print('es negativo')
if numero == 0:
    print('es cero')
'''
'''
num = int(input('digite el numero : '))

if num > 0:
    print('el numero ',num,' es positivo')
if num < 0:
    print('el numero ',num,' es negativo')
if num == 0:
    print('el numero',num,' es cero')
'''

entero = int(input('ingresar el numero entero : '))

if entero < 0:
    entero = entero * (-1)

'''
if entero > 0 and entero < 10:
    print('el numero tiene un digito')
'''

if ((entero >= 0) and (entero <= 9)):
    print('el numero tiene un digito')
    print("termino")
else:
    if ((entero > 9) and (entero <= 99)):
        print("el numero tiene dos digitos")
    else:
        if ((entero > 99) and (entero <= 999)):
            print("el numero tiene tres digitos")
        else:
            if ((entero > 999) and (entero <= 9999)):
                print("el numero tiene cuatro digitos")
            else:
                print("el numero tiene mas de cuatro digitos")
    print("termino")


if ((entero >= 0) and (entero <= 9)):
    print("el numero tiene un digito")
    print("termino")
elif ((entero > 9) and (entero <= 99)):
    print("el numero tiene dos digitos")
    print("termino")
elif ((entero > 99) and (entero <= 999)):
    print("el numero tiene tres digitos")
    print("termino")
elif ((entero > 999) and (entero <= 9999)):
    print("el numero tiene cuatro digitos")
    print("termino")
else:
    print("el numero tiene mas de cuatro digitos")
    print("termino")




def respuesta(n):
    print("el numero tiene", n , "digito(s)")
    print("termino")

entero_len = len(str(entero))
if entero_len == 1:
    respuesta(entero_len)
elif entero_len == 2:
    respuesta(entero_len)
elif entero_len == 3:
    respuesta(entero_len)
elif entero_len == 4:
    respuesta(entero_len)
else:
    print("el numero tiene mas de 4 digitos")
    print("termino")

