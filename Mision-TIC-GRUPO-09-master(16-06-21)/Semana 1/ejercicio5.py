# crear una variable de tipo diccionario
info_persona = {
    'nombre':'',
    'pr_apellido':'',
    'sg_apellido':''
    }

info_persona['nombre'] = input("ingrese el nombre ")
info_persona['pr_apellido'] = input("ingresar el primer apellido ")
info_persona['sg_apellido'] = input("ingresar el segundo apellido ")
info_persona['edad'] = 25

def mostrar_info_personal(var_dict):
    respuesta = "el nombre completo es :" + var_dict['nombre'] + " " + var_dict['pr_apellido'] + " " + var_dict['sg_apellido']
    return respuesta

print(mostrar_info_personal(info_persona))

