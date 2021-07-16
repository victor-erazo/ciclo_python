# Envolturas de funciones

'''
# crear funcion suma
def suma(val1 = 0, val2 = 0):
    return val1 + val2

# funcion puede retornar otra funcion
def operacion(funcion,val1 = 0, val2 = 0):
    return funcion(val1,val2)

# Asignar una funcion a una variable
f_suma = suma

# Funcion utilizando como parametro otra funcion
resultado = operacion(f_suma,45,45)

print(resultado)
'''

def crear_funcion(operador):
    result = 0
    if operador == '+':
        def suma(val1 = 0, val2 = 0):
            return val1 + val2
        return suma
    elif operador == '-':
        def resta(val = 0, val2 = 0):
            return val - val2
            # result = val - val2
        return resta

def operacion(funcion, val1 = 0, val2 = 0):
    return funcion(val1,val2)

funcion_suma = crear_funcion('+')
resultado = operacion(funcion_suma,56,79)
print(resultado)

funcion_resta = crear_funcion('-')
resultado = operacion(funcion_resta,45,40)
print(resultado)
