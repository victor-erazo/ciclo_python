# variables de tipo entero
var_int = 7 
# variable de tipo float o decimal
var_float = 3.6
# variable de tipo cadena de texto
var_texto = "09"
# variable de tipo boolean
var_boo = False

# variable de tipo diccionario
var_dict = {"nombre":"Rafael","apellido":"Canoles","edad":26,"altura": 178}
# editar o modificar campo del diccionario
var_dict['altura'] = 180
# agregar un campo diccionario
var_dict['peso'] = 80.5
# eliminar un campo en el diccionario
var_dict.pop('nombre')

print(var_dict)

'''
print(type(var_int))
print(type(var_float))
print(type(var_texto))
print(type(var_boo))
print(type(var_dict))

var_float = int(var_float) + 5
print(var_float)

var_int = float(var_int)
print(var_int)

var_texto = int(var_texto)
print(var_texto)

var_int = str(var_int)
print("valor es : " + var_int)
'''

miDicc = {
    'nombre': input('ingrese su nombre'),
    'apellido':input('ingrese su apellido'),
    'edad':int(input('ingrese su edad'))
}

print(miDicc)
print(1 + miDicc['edad'])
