# AUTOR YEISON CAMILO MORENO GRUPO 09 MISION TIC 2022
'''
Escriba una función que reciba como parámetro un diccionario en el cual las llaves son los 
nombres de las variables antes mencionadas. Retorne un diccionario con las llaves 
“id_diagnostico”, “resultado” y “estado”. Tenga en cuenta que si el resultado es 1 el mensaje 
debe ser ‘Presencia de síntomas’, o de lo contrario el resultado es 0 el mensaje debe ser ‘No 
tiene síntomas’.
'''
# function


def diagSintoma(paciente: dict) -> dict:
    if paciente["diag_ta"] == "Si":
        if paciente["diag_pa"] == "Si":
            if paciente["diag_do"] == "Si":
                if paciente["diag_dg"] == "Si":
                    return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "Dengue", "estado": True})
                else:
                    return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de síntomas", "estado": False})
            else:
                return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de síntomas", "estado": False})
        else:
            if paciente["diag_do"] == "Si":
                return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de síntomas", "estado": False})
            else:
                if paciente["diag_dg"] == "Si":
                    return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "Gripa", "estado": True})
                else:
                    return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de síntomas", "estado": False})
    else:
        if paciente["diag_pa"] == "Si":
            if paciente["diag_do"] == "Si":
                if paciente["diag_dg"] == "Si":
                    return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "Otitis", "estado": True})
                else:
                    return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de síntomas", "estado": False})
            else:
                return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de síntomas", "estado": False})
        else:
            if paciente["diag_do"] == "Si" or paciente["diag_dg"] == "Si":
                return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de síntomas", "estado": False})
            else:
                return({"id_diagnostico": paciente["id_diagnostico"], "resultado": "No tiene síntomas", "estado": False})

# Diccionarios


sintomas_1 = {
    "id_diagnostico":  "d-001",
    "diag_ta":  "Si",
    "diag_pa":  "No",
    "diag_do":  "No",
    "diag_dg":  "Si"

}

sintomas_2 = {
    "id_diagnostico":  "d-002",
    "diag_ta":  "Si",
    "diag_pa":  "No",
    "diag_do":  "No",
    "diag_dg":  "No"

}

sintomas_3 = {
    "id_diagnostico":  "d-003",
    "diag_ta":  "No",
    "diag_pa":  "No",
    "diag_do":  "No",
    "diag_dg":  "No"

}
