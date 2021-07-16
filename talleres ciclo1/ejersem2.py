#Determinar si dado un número entero, termina en 4(Desiciones en cascada)
'''
a = input("ingrese un numero entero") #Recibe el dato por la terminal

if int(a)/1 == int(a):
    if a[-1] == "4":
        print("termina en 4")
    else:
        print("no termina en 4")
else:
    print("ingrese solo numero")       
'''
# Determine si dado un numero, este tiene tres digitos
'''
b = input("ingrese un numero: ")

if len(b) == 3:
    print("tiene 3 digitos")
else:
    print("no tiene 3 digitos")
'''
# Determine si un numero entero, tiene dos digitos y si ambos digitos son pares
'''
c = int(input("ingrese un numero: "))

if((c >= 10) and (c < 100)) or ((c <=-10)  and (c >-100)):
    if (c)%2 == 0 and int(c*0.1)%2 ==0:
        print("ambas digitos son pares")
    else:
        print("alguno de los 2 no es par")
else:
    print("no es de dos digitos")
'''
#Determina si un numero menor que 20 es primo
'''
c = int(input("ingrese un numero menor que 20: "))

if c<20:
    if ((c==2) or (c==3) or (c==%) or (c==7) or (c==11) or (c==13) or (c==17) or (c==19))
        print(f'{c} es un numero primo')
    else: 
        print(f'{c} no es primo')
else:
    print(f'¿en qué quedamos? Menor que 20')
'''
#veamos si es primo, de dos digitos y negativo
'''
d = int(input("ingrese un numero: "))

def es_primo(d, n=2):
    if n >= d:
        print("Es primo,negativo y de 2 digitos")
        return True
    elif d % n != 0:
        return es_primo(d, n + 1)
    else:
        print(f"{d} No es primo y {n} es divisor")
        return False

if ((d>-100) and (d<-9)):
    print(es_primo(d*-1))
else:
    print(f'{d} no es negativo o de 2 digitos')
'''

#Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales. 
'''
c = int(input("ingrese un numero: "))

if (c>9) and (c<100):
    if int(c*0.1)==int(str(c)[-1]):
        print("tiene 2 cifras y son iguales")
    else:
        print("nada")
else:
    print("no tiene 2 digitos")
'''

#Leer dos números enteros y determinar cuál es el mayor.
'''
a = input("ingrese un numero : ")
b = input("ingrese un numero : ")
print(type(b))

if b > a:
    print(f"{b} es mayor que {a}")
else:
    print(f"{a} es menor que {b}")
'''
#Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.
 #c = 10
 #d = 13
'''
a= "12"
c= "14"
b = list(a)
d = list(c)
print(b)
print(d)
print(sum(int(b), int(d))
for 
'''
#operacion =  c[0] + c[1] + d[0] + d[1]
#c[0] + c[1] + d[0] + d[1]
#listahermosita = [c,d]
'''
num8 = input("Digite primer numero: ")
num9 = input("Digite segundo numero: ")
try:
    if int(num8) >= -99 and int(num8) <= -10:
        num8 = int(num8) * -1
    if int(num9) >= -99 and int(num9) <= -10:
        num9 = int(num9) * -1

    if (int(num8) >= 10 and int(num8) <= 99) and (int(num9) >= 10 and int(num9) <= 99):
        sumNum8 = int(str(num8[0])) + int(str(num8[1]))
        sumNum9 = int(str(num9[0])) + int(str(num9[1]))
        sum2num = sumNum8 + sumNum9
        print("La sumatoria de los digitos del numero", num8, "es:", sumNum8)
        print("La sumatoria de los digitos del numero", num9, "es:", sumNum9)
        print("La sumatoria de todos los digitos es: ", sum2num)
    else:
        print("Los dos numeros deben ser enteros de dos digitos")
except:
    print("Digite numeros enteros")
'''
""" b = input("ingrese numero entero: ")   #repasar estructuras iterativas while y for
a = list(b)
print(a)
for i in range(len(a)):
    a[i] = int(a[i])
print(sum(a)) """

# Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.
#num = input("Digite numero entero: ")


""" b = input("ingrese numero entero: ")   #repasar estructuras iterativas while y for
a = list(b)
print(a)
for i in range(len(a)):
    a[i] = int(a[i])
print(sum(a))

b = '12'
a = list(b)
c= '32'
d = list(c)
print(a)
print(d)
for i in range(len(a)):
    a[i] = int(a[i])
print(sum(a))
for j in range(len(d)):
    d[j] = int(d[j])
print(sum(d))
print(sum(a)+sum(d)) """
""" 
num = int(input("ingrese un numero de tres digitos: "))
x = int(num*0.001)
y = int(num*0.01)
z = int(num*0.1)

if x<y:
    if y<z:
        print(f'{x}<{y}<{z}')
    else:
        print(f'{x}<{z}<{y}')
else:
    if x<z:
        print(f'{y}<{x}<{z}')
    else:
        if y<z:
            print(f'{y}<{z}<{x}')
        else:
            print(f'{z}<{y}<{x}') """

""" num10 = input("Digite numero: ")
try:
    if int(num10) < 0:
        num10 = str(int(num10) * -1)
    if (int(num10) >= 100) and (int(num10) <= 999):
        uno = str(num10[0])
        dos = str(num10[1])
        tres = str(num10[2])
        if (uno > dos) and (uno > tres):
            print("el numero mayor es", uno, "y está en la primera posición")
        elif (dos > uno) and (dos > tres):
            print("el numero mayor es", dos, "y está en la segunda posición")
        elif (tres > uno) and (tres > dos):
            print("el numero mayor es", tres, "y está en la tercera posición")
        else:
            print("No hay un numero mayor")
    else:
        print("Digite numero de 3 digitos")
except:
    print("Digite numeros enteros") """

""" 
vowels = ['a', 'e', 'i', 'o', 'u']

# index of'p' is vowels
index = vowels.index('a')
print('The index of a:', index) """

#Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.
k = list("923")
x = int(k[0]) 
y = int(k[1])
z = int(k[2])

if (x % y == 0) or (y % x ==0): 
    print(f'{x} es un multiplo o divisor de {y}' )
else:
    if (x % z == 0) or (z % x == 0):
        print(f'{x} es un multiplo o divisor de {z}')
    else:
        if (y % z == 0) or (z % y == 0):
            print(f'{y} es un multiplo o divisor de {z}')
        else:
            print("los digitos no son ni divisores ni multiplos entre sí")














