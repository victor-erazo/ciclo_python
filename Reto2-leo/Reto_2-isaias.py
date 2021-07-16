"""
Reto 2

Descripción del problema: En una clínica se requiere analizar los síntomas de nuevos
pacientes para determinar si tiene estos tres tipo de enfermedades (gripa, dengue, otitis),
realice un programa que permita a un medico, determinar si posee una enfermedad,
presenta síntomas o no presenta síntomas; tenga en cuenta que para cada enfermedad
tiene un numero de síntomas relacionados para ser positivo.

Nombre          Tipo    Descripción
id_diagnostico  str     Identificador diagnostico nuevo paciente.
diag_ta         str     Síntoma temperatura alta (‘Si’ / ‘No’)
diag_pa         str     Síntoma presión alta (‘Si’ / ‘No’)
diag_do         str     Síntoma dolor oído (‘Si’ / ‘No’)
diag_dg         str     Síntoma dolor de garganta (‘Si’ / ‘No’)

Además la clínica tiene un modelo basado en arboles de decisión para poder realizar mas
fácilmente el análisis de los síntomas de cada enfermedad respectiva.

Escriba una función que reciba como parámetro un diccionario en el cual las llaves son los
nombres de las variables antes mencionadas. Retorne un diccionario con las llaves
“id_diagnostico”, “resultado” y “estado”. Tenga en cuenta que si el resultado es 1 el
mensaje debe ser‘Presencia de síntomas’ o de lo contrario el resultado es 0 el mensaje debe
ser ‘No tiene síntomas’, además si presenta alguna enfermedad su estado será positivo
(True) de lo contrario su estado es negativo (False).

def diagSintoma(paciente:dict)->dict:
    pass
"""

def diagSintoma(paciente:dict)->dict:
    analisis = {}
    analisis['id_diagnostico'] = paciente['id_diagnostico']
    
    if paciente['diag_ta'] == "Si":
        if paciente['diag_pa'] == "Si":
            if paciente['diag_do'] == "Si":
                if paciente['diag_dg'] == "Si":
                    analisis['resultado'] = 'Dengue'
                    analisis['estado'] = True
                else:
                    analisis['resultado'] = 'Presencia de síntomas'
                    analisis['estado'] = False
            else:
                analisis['resultado'] = 'Presencia de síntomas'
                analisis['estado'] = False
        else:
            if paciente['diag_do'] == "No":
                if paciente['diag_dg'] == "Si":
                    analisis['resultado'] = 'Gripa'
                    analisis['estado'] = True
                else:
                    analisis['resultado'] = 'Presencia de síntomas'
                    analisis['estado'] = False
            else:
                analisis['resultado'] = 'Presencia de síntomas'
                analisis['estado'] = False
    else:
        if paciente['diag_pa'] == "Si":
            if paciente['diag_do'] == "Si":
                if paciente['diag_dg'] == "Si":
                    analisis['resultado'] = 'Otitis'
                    analisis['estado'] = True
                else:
                    analisis['resultado'] = 'Presencia de síntomas'
                    analisis['estado'] = False
            else:
                analisis['resultado'] = 'Presencia de síntomas'
                analisis['estado'] = False
        else:
            if paciente['diag_do'] == "Si" or paciente['diag_dg'] == "Si":
                analisis['resultado'] = 'Presencia de síntomas'
                analisis['estado'] = False
            else:
                analisis['resultado'] = 'No tiene síntomas'
                analisis['estado'] = False
    return analisis

print(diagSintoma())