'''
num = int(input("digite el numero : "))
if num == 0:
    print("el numero no puede ser cero (0)")
elif num < 0:
    print("el numero es negativo")
    num = num * (-1)
    if len(str(num)) == 3:
        print("el numero tiene 3 digitos")
else:
    print("el numero es positivo")
    if len(str(num)) == 2:
        print("el numero tiene 2 digitos")


if num != 23:
    print('numero es diferente')

n = 4
if ((n%2 == 0) or (n%3 == 0)):
    print('correcto')


if 10 and True:
    print('correcto')

x = 3
y = 5

if x < y:
    print('x es menor a y')
elif x > y:
    print('x es mayor a y')
else:
    print('x y y son iguales')
'''

x = 6
y = 7
z = 20

# indique si es mayor , medio y menor de tres variables

if x > y and x > z and y > z:
    print (x, ' es el mayor ', y,' es el medio ',z,' es el menor')
if x > y and x > z and y < z:
    print(x,' es la mayor',z,' es la del medio ',y,' es la menor') 
if y > x and y > z and x > z:
    print(y, ' es le mayor ',x,' es el medio ',z,' es el menor')
if y > x and y > z and x < z:
    print(y,' es la mayor',z,' es la del medio ',x,' es la menor') 
if z > x and z > y and x > y:
    print(z,' es la mayor',x,' es la del medio ',y,' es la menor')
if z > x and z > y and x < y:
    print(z,' es la mayor',y,' es la del medio ',x,' es la menor') 


if x > y and x > z:
    if y > z:
        print(x, ' es el mayor ', y,' es el medio ',z,' es el menor')
    else:
        print(x, ' es el mayor ', z,' es el medio ',y,' es el menor')
elif y > x and y > z:
    if x > z:
        print(y, ' es le mayor ',x,' es el medio ',z,' es el menor')
    else:
        print(y, ' es le mayor ',z,' es el medio ',x,' es el menor')
elif z > x and z > y:
    if x > y:
        print(z,' es la mayor',x,' es la del medio ',y,' es la menor')
    else:
        print(z,' es la mayor',y,' es la del medio ',x,' es la menor')
