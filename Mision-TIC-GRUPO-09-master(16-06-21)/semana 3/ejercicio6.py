
nombres = list() # nombres = []
edades = list() # edades = []
# x = 0
# while x < 5:
for x in range(5):
    m_nombre = "Ingrese el nombre de la persona : " + str(x + 1) + ' -> '
    nombre = input(m_nombre)
    edad = int(input('Ingrese la edad de la persona : '))
    nombres.append(nombre)
    edades.append(edad)

print('Nombre de las personas mayores de edad : ')

print(nombres)
print(edades)

for x in range(len(edades)):
    if edades[x] >= 18:
        print(nombres[x])