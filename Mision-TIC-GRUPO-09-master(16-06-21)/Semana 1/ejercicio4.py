# crear funcion sin parametros
def imprimirMensaje():
    print('Grupo 09') # imprimir una cadena de texto en la consola

# llamando la funcion
# imprimirMensaje()

# crear funcion sin parametros retornar una cadena de texto
def imprimirMensaje_re():
    return('Gurpo 09')

cadena_t = imprimirMensaje_re()
# print(cadena_t)

# print(imprimirMensaje_re())


def suma(var_a,var_b):
    resultado = (var_a + var_b) # operación aritmetica
    # print(resultado)
    return resultado

rta = suma(5,8)
# print(rta)

def resta(var_c,var_d):
    resultado = (var_c - var_d) # operación aritmetica
    return resultado

var_1 = 78
var_2 = 45
rta_r = resta(var_1,var_2)

# convertir las varibles var_1, var_2 var_3 tipo cadena de texto

'''
print("(" + str(var_1) + " - " + str(var_2) + ") = " + str(rta_r))
print( "(" , var_1 , " - " , var_2 , ") = " , rta_r)
print(f"({var_1} - {var_2}) = {rta_r}")
print("({} - {}) = {}".format(var_1,var_2,rta_r))
'''

# print(suma((suma(2,4) * resta(4,5)),100))

def repetirOperaciones():
    print(suma(4,8))
    print(suma(7,2))
    print(resta(6,5))
    print(resta(8,12))

repetirOperaciones()

rta = resta(suma(3,5),suma(5,9))

print(rta)






