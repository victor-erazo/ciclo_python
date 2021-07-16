
# notas 
nota1 = 3.4
nota2 = 4
nota3 = 2
nota4 = 4.2

# funcion que nos permita calcular el promedio de 4 variable(notas)
def calcular_promedio(n1,n2,n3,n4):
    resultado = ((n1 + n2 + n3 + n4) / 4)
    resultado = round(resultado,1)
    return resultado

print(calcular_promedio(nota1, nota2, nota3, nota4))

# como realizar un funcion que calcule el promedio de varios datos
# tener como referencia la funciones de python sum() len()