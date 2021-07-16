"""
Desarrollo de reto # 2
Victor Leandro Erazo Rios - Grupo 09
------------------------------------------------------------------------------
INPUT:  Diccionario {id_diagnostico, diag_ta, diag_pa, diag_do, diag_dg} #TODAS SON STR

PROCESADOR (Funcion): def diagSintoma (paciente : dict)-> dict:

SALIDAS:  {'id_diagnostico': 'd001', 'resultado': 'Gripa', 'estado': True}

  1 = ‘Presencia de síntomas’
  0 = ‘No tiene síntomas’
  (gripa, dengue, otitis)

"""

paciente = {"id_diagnostico": "d-001",
            "diag_ta": "No",
            "diag_pa": "No",
            "diag_do": "No",
            "diag_dg": "No"}


print(paciente)

#var_boo = False


def diagSintoma(paciente: dict) -> dict:

    ##########################################################################
    # Condicionales de Diagnostico

    # ---------------------Condicionales para Dengue y Gripa
    if (paciente["diag_ta"] == "Si"):

        if (paciente["diag_pa"] == "Si"):

            if (paciente["diag_do"] == "Si"):

                if (paciente["diag_dg"] == "Si"):  # --DENGUE
                    return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'Dengue', 'estado': True}
                else:
                    return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'Presencia de síntomas', 'estado': False}
                    # DUDA con Estado!!!!!

            else:  # 1 --DENGUE
                return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'Presencia de síntomas', 'estado': False}
                # DUDA con Estado!!!!!

        else:

            if (paciente["diag_do"] == "Si"):  # 1 --GRIPA
                return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'Presencia de síntomas', 'estado': False}
                # DUDA con Estado!!!!!
            else:
                if (paciente["diag_dg"] == "Si"):  # --GRIPA
                    return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'Gripa', 'estado': True}

                else:  # 1 --GRIPA
                    return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'Presencia de síntomas', 'estado': False}
                # DUDA con Estado!!!!!

    # ---------------------Condicionales para Otitis
    else:
        if (paciente["diag_pa"] == "Si"):

            if (paciente["diag_do"] == "Si"):

                if (paciente["diag_dg"] == "Si"):
                    return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'Otitis', 'estado': True}
                    # DUDA LA ENFERMEDAD SI PONGO MAYUSCULAS....:!!!

                else:  # 1 --Otitis
                    return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'Presencia de síntomas', 'estado': False}
                # DUDA con Estado!!!!!

            else:  # 1 --Otitis
                return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'Presencia de síntomas', 'estado': False}
                # DUDA con Estado!!!!!

        elif (paciente["diag_do"] == "No" and paciente["diag_dg"] == "No"):
            return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'No tiene síntomas', 'estado': False}
            # DUDA con Estado!!!!!

        else:
            return {'id_diagnostico': paciente["id_diagnostico"], 'resultado': 'Presencia de síntomas', 'estado': False}
            # DUDA con Estado!!!!!


print(diagSintoma(paciente))
