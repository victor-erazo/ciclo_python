temperatura_fahr = input('ingrese la temperatura en grados fahrenheit : ')
try:
    fahr = float(temperatura_fahr)
    cel_g = (fahr - 32.0) * 5.0 / 9.0
    print(cel_g)
except:
    print('ingrese un numero')