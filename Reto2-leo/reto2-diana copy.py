# Diccionario
paciente = {
    "id_diagnostico": "d001",
    "diag_ta": "Sí ",
    "diag_pa": "Sí ",
    "diag_do": "Sí ",
    "diag_dg": "Sí "
}
print(paciente)


def diagSintoma(paciente: dict) -> dict:
    #resultado = {"id_diagnostico" : " ", "resultado" : " ", "estado" : " "}
    #resultado = {}

    if paciente["diag_ta"] == "Sí":
        if paciente["diag_pa"] == "Sí":
            if paciente["diag_do"] == "Sí":
                if paciente["diag_dg"] == "Sí":
                    return {
                        "id_diagnostico": paciente["id_diagnostico"], "resultado": "Dengue", "estado": True}
                    # return resultado
                else:
                    return {
                        "id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de síntomas", "estado": True}
                    # return resultado
            else:
                return {"id_diagnostico": paciente["id_diagnostico"],
                        "resultado": "Presencia de síntomas", "estado": True}
                # return resultado
        else:
            if paciente["diag_do"] == "Sí":
                return {"id_diagnostico": paciente["id_diagnostico"],
                        "resultado": "Presencia de síntomas", "estado": True}
                # return resultado
            else:
                if paciente["diag_dg"] == "Sí":
                    return {
                        "id_diagnostico": paciente["id_diagnostico"], "resultado": "Gripa", "estado": True}
                    # return resultado
                else:
                    return {
                        "id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de síntomas", "estado": True}
                    # return resultado
    else:
        if paciente["diag_pa"] == "Sí":
            if paciente["diag_do"] == "Sí":
                if paciente["diag_dg"] == "Sí":
                    return {
                        "id_diagnostico": paciente["id_diagnostico"], "resultado": "Otitis", "estado": True}
                    # return resultado
                else:
                    return {
                        "id_diagnostico": paciente["id_diagnostico"], "resultado": "Presencia de síntomas", "estado": True}
                    # return resultado
            else:
                return {"id_diagnostico": paciente["id_diagnostico"],
                        "resultado": "Presencia de síntomas", "estado": True}
                # return resultado
        else:
            if (paciente["diag_do"] == "Sí") or (paciente["diag_dg"] == "Sí"):
                return {"id_diagnostico": paciente["id_diagnostico"],
                        "resultado": "Presencia de síntomas", "estado": True}
                # return resultado
            if (paciente["diag_do"] == "Sí") or (paciente["diag_dg"] == "No"):
                return {"id_diagnostico": paciente["id_diagnostico"],
                        "resultado": "Presencia de síntomas", "estado": True}
                # return resultado
            if (paciente["diag_do"] == "No") or (paciente["diag_dg"] == "Sí"):
                return {"id_diagnostico": paciente["id_diagnostico"],
                        "resultado": "Presencia de síntomas", "estado": True}
                # return resultado
            if (paciente["diag_do"] == "No") or (paciente["diag_dg"] == "No"):
                return {
                    "id_diagnostico": paciente["id_diagnostico"], "resultado": "No tiene síntomas", "estado": False}
                # return resultado
    # return resultado


print(diagSintoma(paciente))
