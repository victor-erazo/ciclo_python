# Funciones anonimas (lambda)

'''
def suma(val1=0,val2=0):
    return val1 + val2
'''

'''
suma = lambda val1 = 0, val2 = 0 : val1 + val2
operacion = lambda operacion,val1 = 0, val2 = 0 : operacion(val1,val2)
resultado = operacion(suma,6,4)
print(resultado)
'''

'''
sin_parametros = lambda : True
# print(sin_parametros() == False)

con_valores = lambda val = 1 , val1 = 1, val2 = 1 : val + val1 + val2
# print(con_valores())
'''

'''
con_asteristos = lambda * args : args[-1]
lista = [1,2,3,4]
print(con_asteristos(* lista))

tupla = 5,6,7,8,9
print(con_asteristos(* tupla))
'''

tupla = (5,6,7,8,9)
def suma_args(* args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

# print(suma_args(*tupla))

sumatoria = lambda * args : suma_args(* args)
print(sumatoria(* tupla))
