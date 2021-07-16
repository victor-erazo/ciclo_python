"""
Desarrollo de reto # 3
Victor Leandro Erazo Rios - Grupo 09
------------------------------------------------------------------------------

INPUT: Diccionario "creditos"
        Como atributos considerar datos de las tablas de variables

PROCESADOR (Funcion): funcion
    Esqueleto:
        def calcularInforme(creditos : dict)-> list:

SALIDAS:  Lista  return "SIN NOMBRE"
   Formato de salida= [codigoUsuarios,(totPagados,totVencidos,totElaborados)]
   Ejemplo de salida= ['2015020192098-J-A', (1776267.1, 1236997.52, 820405.38)]

'''
{} llaves
[] corchetes
() parentesis
'''


"""

from typing import List


creditos = {
    '2018015647382': {
        'nombres': 'Luis Antonio',
        'apellidos': 'Lopez Rueda',
        'est_credito': 'Activo',
        'credito': [
            {
                'id_credito': 'C0013453',
                'cuotas': 60,
                'valor': 87558500,
                'interes': 0.020,
                'cuo_vencidas': 30,
                'cuo_pagadas': 7
            }
        ]
    },
    '2019041209845': {
        'nombres': 'Elias',
        'apellidos': 'Diaz Lopez',
        'est_credito': 'Activo',
        'credito': [
            {
                'id_credito': 'C0335501',
                'cuotas': 3,
                'valor': 87558,
                'interes': 0.020,
                'cuo_vencidas': 1,
                'cuo_pagadas': 2
            }
        ]
    }

}


def calcularInforme(creditos: dict) -> list:

    # ============================ ESTRUCTURA DE CONTENEDORES DE DATOS:
    for cod, datos in creditos.items():

        valor_credito = creditos[cod]["credito"][0]["valor"]
        cuotas = creditos[cod]["credito"][0]["cuotas"]

        vlr_cuota = []
        valor_cuota = datos["credito"][0]["cuota"] = vlr_cuota

        num_cuota = []
        datos["credito"][0]["lista cuota"] = num_cuota

        vlr_saldo = []
        datos["credito"][0]["lista saldo"] = vlr_saldo

        # ===================================== SECCION DE CALCULOS
        for i in range(cuotas):
            vlr_cuota.append(valor_credito / cuotas)
            num_cuota.append(i)

            if (cuotas == 0):
                vlr_saldo.append(valor_credito-vlr_cuota[0])
            #print("saldito:", vlr_saldo)
            if (cuotas > 0):
                vlr_saldo.append(vlr_saldo[0]-sum(vlr_cuota))

                #saldito = valor_credito-vlr_cuota[0]
                # vlr_saldo.append(saldito)

    return creditos


print(calcularInforme(creditos))
