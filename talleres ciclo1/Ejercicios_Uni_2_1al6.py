# Determinar si dado un entero, éste termina en 4
'''
Tenemos que responder 3 cosas
1ro. Que el dato sea un número. TRY - EXCEPT
2do. Que se un número entero. Toca recibir el dato como Tipo INT
3ro. Que este termine en 4. Verificar bajo un IF (si termina en 4)


a = input('ingrese un número entero: ')  # Recibe el dato por consola

if a[-1]=="4":
    print('Termina en 4')
else:
    print('No termina en 4')

'''
# Determine si dado un número, éste tiene 3 dígitos
'''
b = input('Ingrese un número: ')

if len(b)==3:
    print('Tiene 3 dígitos')
else:
    print('No tiene 3 dígitos')
'''

# Determine si dado un número, tiene 2 cifras y si ambas cifras son pares.
""" 
c = int(input('Ingrese un número: '))

if ((c>=10) and (c<100)) or ((c<=-10) and (c>-100)):
    if c%2==0 and int(c*0.1)%2==0:
        print('Ambas dígitos son pares')
    else:
        print('Alguno de los 2 no es par')
else:
    print('No es de 2 dígitos')
 """

# Determine si un número menor que 20 es primo
'''
c = int(input('Ingrese un número menor que 20: '))

if c<20:
    if((c==2) or(c==3) or (c==5) or (c==7) or (c==11) or (c==13) or (c==17) or (c==19)):
        print(f'{c} es un número primo')
    else:
        print('{c} no es primo')
else:
    print(f'¿En qué quedamos? Menor que 20')
'''
# Veamos si es Primo, de 2 cifras y negativo negativo
'''
d = int(input('Ingrese un número: '))

def es_primo(d, n=2):
    if n >= d:
        print("Es primo, negativo y de 2 dígitos")
        return True
    elif d % n != 0:
        return es_primo(d, n + 1)
    else:
        print(f"{d} no es primo y {n} es divisor")
        return False

if ((d>-100) and (d<-9)):
    print(es_primo(d*-1))
else:
    print(f'{d} no es Negativo o de 2 dígitos')
'''

# Leer un número entero de dos dígitos y
# determinar si los dos dígitos son iguales. 
'''
c = int(input('Ingrese un número: '))

if (c>9) and (c<100):
    if int(c*0.1)==int(str(c)[-1]):
        print('Tiene 2 cifras y son iguales')
    else:
        print('Nada')
else:
    print('No tiene 2 cifras')
'''