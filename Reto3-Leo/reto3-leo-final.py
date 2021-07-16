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
    calc_elaborados = 0
    calc_vencidos = 0
    calc_pagados = 0
    # ============================ ESTRUCTURA DE CONTENEDORES DE DATOS:
    for cod, datos in creditos.items():

        valor_credito = creditos[cod]["credito"][0]["valor"]
        cuotas = creditos[cod]["credito"][0]["cuotas"]

        valor_cuota = datos["credito"][0]["cuota"] = valor_credito / cuotas

        interes_cred = datos["credito"][0]["interes"]

        cuotas_pagas = datos["credito"][0]["cuo_pagadas"]
        cuotas_vencidas = datos["credito"][0]["cuo_vencidas"]

        # Verficacion de variables basicas ==========================
        print("valor credito: ", valor_credito)
        print("cuotas: ", cuotas)
        print("valor cuota: ", valor_cuota)
        print("interes credito: ", interes_cred)

        vlr_interes = 0
        vlr_saldo = 0
        # ===================================== SECCION DE CALCULOS

        vlr_interes = valor_credito*interes_cred
        vlr_saldo = valor_credito - valor_cuota
        print("valor interes en 1: ", vlr_interes)
        print("valor saldo en 1: ", vlr_saldo)
        vlr_pagar = 0
        vlr_pagar += vlr_interes+valor_cuota
        creditos[cod]["credito"][0]["primer pago"] = vlr_pagar

        print("primer pago cada credito: ",
              creditos[cod]["credito"][0]["primer pago"])

        for i in range(1, cuotas):

            vlr_interes = (vlr_saldo*interes_cred)
            vlr_saldo = vlr_saldo-valor_cuota
            print(f"interes cuota {i+1}: ", vlr_interes)
            print(f"saldo cuota {i+1}: ", vlr_saldo)

            #vlr_pagar = vlr_interes+valor_cuota
            #print(f"valor pagar {i+1}: ", vlr_pagar)

            if i < cuotas_pagas:

                calc_pagados += (vlr_interes+valor_cuota)
                totPagados = calc_pagados + vlr_pagar
                #print(f"valor pagar {i+1}: ", vlr_pagar)

            if (cuotas_pagas-1 < i < (cuotas_pagas+cuotas_vencidas)):
                calc_vencidos += (vlr_interes+valor_cuota)
                totVencidos = calc_vencidos

            if (cuotas_pagas+cuotas_vencidas-1) < i < cuotas:
                calc_elaborados += (vlr_interes+valor_cuota)
                totElaborados = calc_elaborados

    #print("verifi vlr pagar:", vlr_pagar)
        print("pruebra pagadas:", calc_pagados)
    print("salidas totales:", totPagados, totVencidos, totElaborados)


print(calcularInforme(creditos))
