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

    # / ////////////////////////////////////////////
    # PARAMETROS INICIALES DE PROCESAMIENTO DE INFORMACION
    list_cod = list()
    list_nombres = list()
    list_apellidos = list()

    list_time_credito = list()
    list_valor_credito = list()
    list_tasa_interes = list()
    list_cuo_vencidas = list()
    list_cuo_pagadas = list()
    list_inicial_nombre = list()
    list_inicial_apellido = list()
    list_valor_cuota = list()

    num_cuota = []
    vlr_cuota = []
    vlr_saldo = []

    y = 0
    for x in (creditos.keys()):
        list_cod.append(x)

        list_nombres.append(creditos[list_cod[y]]['nombres'])
        list_apellidos.append(creditos[list_cod[y]]['apellidos'])
        list_time_credito.append(creditos[list_cod[y]]['credito'][0]['cuotas'])
        list_valor_credito.append(creditos[list_cod[y]]['credito'][0]['valor'])
        list_tasa_interes.append(
            creditos[list_cod[y]]['credito'][0]['interes'])
        list_cuo_vencidas.append(
            creditos[list_cod[y]]['credito'][0]['cuo_vencidas'])
        list_cuo_pagadas.append(
            creditos[list_cod[y]]['credito'][0]['cuo_pagadas'])

        # ========================== captura de iniciales
        nombres = creditos[list_cod[y]]['nombres']
        inicial_nombre = nombres[0]
        list_inicial_nombre.append(inicial_nombre)

        apellidos = creditos[list_cod[y]]['apellidos']
        inicial_apellidos = apellidos[0]
        list_inicial_apellido.append(inicial_apellidos)

        # ================================ Definicion Valor Cuota
        valor_cuota = list_valor_credito[y] / list_time_credito[y]
        list_valor_cuota.append(valor_cuota)

        y = y+1  # contador de ciclo FOR para recoleccion de datos
    print("LISTADO CODIGOS:", list_cod)
    print("LISTADO NOMBRES:", list_nombres)
    print("LISTADO APELLIDOS:", list_apellidos)
    print("LISTADO CUOTAS (tiempo credito):", list_time_credito)
    print("LISTADO VALOR CREDITO:", list_valor_credito)
    print("LISTADO TASA INTERES:", list_tasa_interes)
    print("LISTADO CUOTAS VENCIDAS:", list_cuo_vencidas)
    print("LISTADO CUOTAS PAGADAS:", list_cuo_pagadas)
    print("LISTADO INICIAL NOMBRE:", list_inicial_nombre)
    print("LISTADO INICIAL APELLIDOS:", list_inicial_apellido)
    print("LISTADO VALOR CUOTA:", list_valor_cuota)
    print("LISTADO VALOR SALDO:", list_valor_cuota)
    """
    codigo_inicial = str(list_cod[0])
    # testigo de que tomo codigo credito
    print("codigo_inicial:", codigo_inicial)

    nombres = creditos[list_cod[0]]['nombres']
    inicial_nombre = nombres[0]
    print("inicial nombre:", inicial_nombre)

    apellidos = creditos[codigo_inicial]['apellidos']
    inicial_apellidos = apellidos[0]
    print("inicial apellido:", inicial_apellidos)

    tiempo_credito = creditos[codigo_inicial]['credito'][0]['cuotas']
    valor_credito = creditos[codigo_inicial]['credito'][0]['valor']
    tasa_interes = creditos[codigo_inicial]['credito'][0]['interes']
    cuo_vencidas = creditos[codigo_inicial]['credito'][0]['cuo_vencidas']
    cuo_pagadas = creditos[codigo_inicial]['credito'][0]['cuo_pagadas']

    print("TIEMPO CREDITO: ----- pilas", tiempo_credito)
    """

    # / ////////////////////////////////////////////
    for w in (list_cod):

        if list_cod[0] != "":

            # Valor cuota mensual base
            #valor_cuota = valor_credito / tiempo_credito
            # valor_cuota
    i = 0
    num_cuota = []
    vlr_cuota = []
    vlr_saldo = []
    #vlr_saldo[0] = valor_credito
    vlr_saldo.append(valor_credito-valor_cuota)
    print("impresion deuda inicial credito:", vlr_saldo)
    vlr_interes = []
    vlr_interes.append(valor_credito*tasa_interes)
    print("valor interes inicial:", vlr_interes)
    vlr_pagar = []
    vlr_pagar.append(valor_cuota+valor_credito*tasa_interes)
    print("valor inicial pagar:", vlr_pagar)
    prueba_compuesta = []
    i = 0
    for i in range(tiempo_credito-1):
        i = i+1
        num_cuota.append(i)  # Numero cuota
        vlr_cuota.append(valor_cuota)  # Valor cuotas
        if (i > 0):
            # Deficionde saldo pendiente adeudado
            #vlr_saldo.append(valor_credito - sum(vlr_pagar))
            vlr_saldo.append(vlr_saldo[0] - sum(vlr_cuota))
            #print("suma valor a pagar:", sum(vlr_pagar))
            print("ciclo saldo superior a 1:", vlr_saldo)
            # Definicion valor interes en lista iterable
            vlr_interes.append(tasa_interes*vlr_saldo[i-1])
            print("ciclo interes superior a 1:", vlr_interes)
            # valor a pagar mes a mes
            #pago_mensual = vlr_interes[i]+vlr_cuota[i]
            pago_mensual = vlr_interes[i]+valor_cuota
            vlr_pagar.append(pago_mensual)

    prueba_compuesta
    prueba_compuesta = [num_cuota, vlr_cuota,
                        vlr_interes, vlr_pagar, vlr_saldo]

    print("============ DESPEJE DE LA LOCURA===========")
    print("//////////////////////////////////////////////")
    print("cuotas:", num_cuota)
    print("=================================================")
    print("valor cuotas:", vlr_cuota)
    print("=================================================")
    print("valor interes:", vlr_interes)
    print("=================================================")
    print("valor a pagar:", vlr_pagar)
    print("=================================================")
    print("valor a pagar:", vlr_saldo)
    print("////////////////// cierre detalles //////////////////")

    """
    ######################################
    # ALERTA TENGO UN PROBLEMA EN EL NUMERO DE ITEMS DE AMORTIZACION DE CREDITO
    """

    # Calculos de variables de salida:

    # =============================================  totPagados
    totPagados = sum(vlr_pagar[0:cuo_pagadas])
    print("totPagados:", totPagados)

    # =============================================  totVencidos
    totVencidos = sum(vlr_pagar[cuo_pagadas:cuo_pagadas+cuo_vencidas])
    print("totVencidos:", totVencidos)
    # =============================================  totElaborados
    totElaborados = sum(vlr_pagar[cuo_pagadas+cuo_vencidas:tiempo_credito])
    print("totElaborados:", totElaborados)

    # ==============================================  codigoUsuarios

    codigoUsuarios = f"{codigo_inicial}-{inicial_nombre}-{inicial_apellidos}"
    print(codigoUsuarios)
    # ///////////////////////////////////////////////////////////////////
    # =========== SALIDA DE RETORNO ====================================
    # //////////////////////////////////////////////////////////////////
    estado_credito = tuple()
    estado_credito = totPagados, totVencidos, totElaborados
    # La salida basica sin codigo usuario
    #estado_credito.__add__(totPagados, totVencidos, totElaborados)

    salida_unidad = list()
    salida_unidad.append(codigoUsuarios)
    salida_unidad.append(estado_credito)
    return salida_unidad


print("====-- salida --====")
print(calcularInforme(creditos))
