# Diccionario
paciente = {
    "id_diagnostico": "d001",
    "diag_ta": "No",
    "diag_pa": "No",
    "diag_do": "No",
    "diag_dg": "Si"
}


def diagSintoma(paciente: dict) -> dict:
    resultado = {}

    if paciente["diag_ta"] == "Si":
        if paciente["diag_pa"] == "Si":
            if paciente["diag_do"] == "Si":
                if paciente["diag_dg"] == "Si":
                    resultado = {
                        "id_diagnostico": paciente["id_diagnostico"], "resultado": "Dengue", "estado": True}
                    return resultado
                else:  # no tiene DG
                    resultado = {
                        "id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de Sintomas", "estado": False}
                    return resultado
            else:  # no tiene DO
                resultado = {"id_diagnostico": paciente["id_diagnostico"],
                             "resultado": "Presencia de Sintomas", "estado": False}
                return resultado
        else:  # no tiene PA
            if paciente["diag_do"] == "Si":
                resultado = {"id_diagnostico": paciente["id_diagnostico"],
                             "resultado": "Presencia de Sintomas", "estado": False}
                return resultado
            elif paciente["diag_dg"] == "Si":  # GRIPA:
                # if paciente["diag_dg"] == "Si":  # GRIPA
                resultado = {
                    "id_diagnostico": paciente["id_diagnostico"], "resultado": "Gripa", "estado": True}
                return resultado
            else:
                resultado = {
                    "id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de Sintomas", "estado": False}
                return resultado
                # Acabe brazo del "Si"
    else:
        if paciente["diag_pa"] == "Si":
            if paciente["diag_do"] == "Si":
                if paciente["diag_dg"] == "Si":
                    resultado = {
                        "id_diagnostico": paciente["id_diagnostico"], "resultado": "Otitis", "estado": True}
                    return resultado
                else:  # NO DG
                    resultado = {
                        "id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de Sintomas", "estado": False}
                    return resultado
            else:  # No DO
                resultado = {"id_diagnostico": paciente["id_diagnostico"],
                             "resultado": "Presencia de Sintomas", "estado": False}
                return resultado

        elif (paciente["diag_do"] == "No") and (paciente["diag_dg"] == "No"):
            resultado = {
                "id_diagnostico": paciente["id_diagnostico"], "resultado": "No tiene Sintomas", "estado": False}
            return resultado
        else:
            resultado = {"id_diagnostico": paciente["id_diagnostico"],
                         "resultado": "Presencia de Sintomas", "estado": False}
            return resultado

        """
        elif (paciente["diag_do"] == "Si") or (paciente["diag_dg"] == "Si"):
            # if (paciente["diag_do"] == "Si") or (paciente["diag_dg"] == "Si"):
            resultado = {"id_diagnostico": paciente["id_diagnostico"],
                         "resultado": "Presencia de Sintomas", "estado": True}
            return resultado
        
        elif (paciente["diag_do"] == "Si") or (paciente["diag_dg"] == "No"):
            resultado = {"id_diagnostico": paciente["id_diagnostico"],
                         "resultado": "Presencia de Sintomas", "estado": True}
            return resultado
        elif (paciente["diag_do"] == "No") or (paciente["diag_dg"] == "Si"):
            resultado = {"id_diagnostico": paciente["id_diagnostico"],
                         "resultado": "Presencia de Sintomas", "estado": True}
            return resultado
        # (paciente["diag_do"] == "No") or (paciente["diag_dg"] == "No"):
        """
        """"
        else:
            # elif (paciente["diag_do"] == "No") and (paciente["diag_dg"] == "No"):
            resultado = {
                "id_diagnostico": paciente["id_diagnostico"], "resultado": "No tiene Sintomas", "estado": False}
            return resultado

            """
    # return resultado


print(diagSintoma(paciente))
