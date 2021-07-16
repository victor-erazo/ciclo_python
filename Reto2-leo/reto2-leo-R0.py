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

paciente = {"id_diagnostico": "", "diag_ta": "",
            "diag_pa": "", "diag_do": "", "diag_dg": ""}
print(paciente)

#var_boo = False


def diagSintoma(paciente: dict) -> dict:

    # ====================================Definicion de condiciones booleanas
    if (paciente["diag_ta"] == "Si"):
        diag_ta = True
    else:
        diag_ta = False

    if (paciente["diag_pa"] == "Si"):
        diag_pa = True
    else:
        diag_pa = False

    if (paciente["diag_do"] == "Si"):
        diag_do = True
    else:
        diag_do = False

    if (paciente["diag_dg"] == "Si"):
        diag_dg = True
    else:
        diag_dg = False

    ##########################################################################
    # Condicionales de Diagnostico

    # ---------------------Condicionales para Denge y Gripa
    if (diag_ta=True):

        if (diag_pa=True):

            if (diag_do=True):

                if (diag_dg=True):
                    return paciente = {'id_diagnostico': 'd001', 'resultado': 'Gripa', 'estado': True}

                    # ---------------------Condicionales para Otitis
    else:
