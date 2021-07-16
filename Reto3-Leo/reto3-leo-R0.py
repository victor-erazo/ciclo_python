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
print(creditos)
print("===================================")
# print(creditos['credito'][0]['valor'])
prueba = creditos['2015020192098']
print(prueba)
print("===================================")
print("===================================")
print(creditos['2015020192098']['credito'][0]['valor'])

tiempo_credito = creditos['2015020192098']['credito'][0]['cuotas']
valor_credito = creditos['2015020192098']['credito'][0]['valor']
tasa_interes = creditos['2015020192098']['credito'][0]['interes']


def calcularInforme(creditos: dict) -> list:

    # Valor cuota mensual base
    valor_cuota = valor_credito / tiempo_credito
    valor_cuota
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
    
    ######################################
    # ALERTA TENGO UN PROBLEMA EN EL NUMERO DE ITEMS DE AMORTIZACION DE CREDITO
    
    
    return prueba_compuesta
    # return tiempo_credito = creditos['2015020192098']['credito'][0]['cuotas']

    # Analisis de rubros mensuales
    #valor_credito = creditos['credito'][0]['valor']
    # return valor_credito

    # totPagados

    # totVencidos

    # totElaborados


print("====-- salida --====")
print(calcularInforme(creditos))
