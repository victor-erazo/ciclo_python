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

"""
creditos = {
    '2015020192098': {
        'nombres': 'Juan',
        'apellidos': 'Arias Ruiz',
        'est_credito': 'Activo',
        'credito': [
            {
                'id_credito': 'C0198238',
                'cuotas': 24,
                'valor': 3066936.00,
                'interes': 0.020,
                'cuo_vencidas': 8,
                'cuo_pagadas': 10
            }
        ]
    }
}
"""


def calcularInforme(creditos: dict) -> list:

    # ================================ # variables de salida
    totPagados = 0
    totVencidos = 0
    totElaborados = 0
    codigoUsuarios = ""

    vlr_pagar = 0
    vlr_interes = 0

    # ============================ ESTRUCTURA DE CONTENEDORES DE DATOS:
    for cod, datos in creditos.items():

        if datos["est_credito"] == "Activo":

            valor_credito = creditos[cod]["credito"][0]["valor"]
            cuotas = creditos[cod]["credito"][0]["cuotas"]

            valor_cuota = datos["credito"][0]["cuota"] = valor_credito / cuotas

            interes_cred = datos["credito"][0]["interes"]

            cuotas_pagas = datos["credito"][0]["cuo_pagadas"]
            cuotas_vencidas = datos["credito"][0]["cuo_vencidas"]
            """
            # Verficacion de variables basicas ==========================
            print("valor credito: ", valor_credito)
            print("cuotas: ", cuotas)
            print("valor cuota: ", valor_cuota)
            print("interes credito: ", interes_cred)
            """
            # ============================== SECCION PARA AJUSTE DE CODIGOS E INICIALES

            """
            saco iniciale y creo una cadena de texto iterativa con incremento
            """

            nombre = datos["nombres"]
            ini_nombre = nombre[0]

            apellido = datos["apellidos"]
            ini_apellido = apellido[0]

            codigo_uno = f"{cod}-{ini_nombre}-{ini_apellido}"+"-"
            codigoUsuarios += codigo_uno

            # ============================== Iteraciones para CALCULOS TOTALES
            for i in range(cuotas):
                """ CON ESTA ITERACION ACTUALIZO SALDOS Y VALORES DE PAGO"""
                # deficion de valor a pagar INTERESES por cada cuota (Actualiza saldo credito)
                vlr_interes = valor_credito * interes_cred
                # Actualizacion del saldo credito restandole cuota mensual
                valor_credito -= valor_cuota
                # Valor a pagar mes a mes con intereses
                vlr_pagar = valor_cuota+vlr_interes

                if (i < cuotas_pagas):  # sin  = para no tener iteracion extra
                    totPagados += vlr_pagar

                # sin  = para no tener iteracion extra
                if (cuotas_pagas <= i < (cuotas_pagas+cuotas_vencidas)):
                    totVencidos += vlr_pagar

                # sin  = para no tener iteracion extra
                if (cuotas_pagas+cuotas_vencidas <= i < cuotas):
                    totElaborados += vlr_pagar

            # ============================ CONSTRUCCION DE SALIDA
    informe_creditos = tuple()
    informe_creditos = (round(totPagados, 2), round(
        totVencidos, 2), round(totElaborados, 2))

    balance_creditos = list()
    balance_creditos = [codigoUsuarios[:-1], informe_creditos]

    return balance_creditos
    #print("prueba valor a pagar: ", vlr_pagar)
    #print("tupla salida: ", informe_creditos)

# calcularInforme(creditos)
