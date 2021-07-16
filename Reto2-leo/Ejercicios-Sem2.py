
# Leer un número entero y determinar si es un número terminado en 4.

'''
{} llaves
[] corchetes
() parentesis
'''
numero = str(20854)

cifras = int(len(numero))
print("numero cifras:", cifras)

ult_cifra = int(numero[cifras-1])  # Recuerda que cuenta cero, debo restar 1
print("ultima cifra:", ult_cifra)

# formato_cifra = int(ult_cifra)

if (ult_cifra == 4):
    print("SI termina en 4 el numero")

else:
    print("NO termina en 4 el numero")

print("============PUNTO 2======================")

##################################################################################
# Leer un número entero y determinar si tiene 3 dígitos.

numero2 = str(204)

cifras2 = int(len(numero2))
print("numero cifras:", cifras2)

if (cifras2 == 3):
    print("SI tiene 3 digitos")

else:
    print("NO tiene 3 digitos")
print("===========PUNTO 3=====================")

################################################################################
# Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

numero3 = str(48)

cifras3 = int(len(numero3))
print("numero cifras:", cifras3)

digito1 = int(numero3[0])
print("digito1:", digito1)
digito2 = int(numero3[1])
print("digito2:", digito2)

verif1 = digito1 / 2
verif2 = digito2 / 2
if (digito1 % 2 == 0 and digito2 % 2 == 0):  # Residuo cero

    print("Los dos digitos SON pares")

else:
    print("NO son pares los digitos")

print("===============PUNTO 4====================")

################################################################################
# Leer un número entero de dos dígitos menor que 20 y determinar si es primo.

# número primo Número entero que solamente es divisible por él mismo (positivo y negativo)
# y por la unidad (positiva y negativa).

valor = 3


def es_primo(valor):
    for n in range(2, valor):
        if valor % n == 0:
            print("No es primo, YA QUE", n, "es divisor")
            return False
    print("Es Numero PRIMO")
    return True


es_primo(valor)

print("=============PUNTO 5=======================")

################################################################################
# Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.

valor2 = -13


def es_primo2(valor2):
    for n in range(2, valor2):
        if valor2 % n == 0 or valor2 > 0:
            print("NO cumple condiciones de PRIMO Y NEGATIVO")
            return False
    print("CUMPLE CONDICIONES DE PRIMO Y NEGATIVO")
    return True


es_primo2(valor2)

print("============PUNTO 6===================")

################################################################################
# Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.

number = str(88)

if (int(number[1]) == int(number[0])):
    print("cifras de igual valor")

else:
    print("cifras diferente valor")

print("============PUNTO 7===================")

################################################################################
# Leer dos números enteros y determinar cuál es el mayor.

number = str(89)

if (int(number[1]) > int(number[0])):
    print("Digito 2 mayor que Digito 1")

else:
    print("Digito 1 mayor que Digito 2")

print("============PUNTO 8===================")

################################################################################
# Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos
# los dígitos.+


print("============PUNTO 23===================")

################################################################################
# Diseñe una calculadora que sume, reste, multiplique y divida, la cual le pida al usuario
# mediante input el valor del primer número, el valor del segundo número y la operación a
# realizar, hay que tener en cuenta la validación de los valores de entrada, por ejemplo:

# Si el programa pide el primer valor, y el usuario ingresa una letra, combinaciones de
# números y letras o caracteres no numéricos se debe mostrar un mensaje mediante otro input
# requiriendo que ingrese nuevamente el numero e indicándole al usuario que el carácter
# ingresado debe ser numérico.
# En el caso que uno de los valores ingresados sea 0 y el usuario ingrese la opción de
# División, debe imprimir un mensaje donde se indique que no se pude dividir entre cero o
# que el cero no puede ser dividido.
# Recomendaciones para la validación: buscar información en Google sobre valores ASCII
# y tabla ASCII investigue el funcionamiento de la función ord()


def entrada1():
    while True:
        num_entrada1 = (input("numero 1:"))  # Ojo aca no convertir a INT

        try:
            num_entrada1 = int(num_entrada1)
            print("dato1 recibido")
            return (num_entrada1)

        except ValueError:
            print("pone el numero bien campeon!!")


def entrada2():
    while True:
        num_entrada2 = (input("numero 2:"))  # Ojo aca no convertir a INT
        try:
            num_entrada2 = int(num_entrada2)
            print("dato2 recibido")
            return num_entrada2

        except ValueError:
            print("pone el numero bien campeon!!")


entrada1()
entrada2()


"""
num_entrada1 = int(input("numero 1:"))
print(num_entrada1)
while (num_entrada1 % 1 != num_entrada1):

    print("pone el numero bien campeon!!")
    num_entrada1 = int(input("numero 1:"))

print("dato1 recibido")

num_entrada2 = int(input("numero 2:"))
while (num_entrada2 % 1 != num_entrada2):

    print("pone el numero bien campeon!!")

print("dato2 recibido")

operacion = input(
    "Digite que operacion hacer (suma, resta, multiplicacion, division):")

"""
