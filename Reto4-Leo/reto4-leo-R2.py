"""
Desarrollo de reto # 4
Victor Leandro Erazo Rios - Grupo 09
------------------------------------------------------------------------------

INPUT: Diccionarios: - id_predio
                     - diccionario consumo
                     - plan tarifario estatico

        Como atributos considerar datos de las tablas de variables

PROCESADOR (Funcion): funcion recibo dos diccionarios
    Esqueleto:
        def inforServicio(lectura : dict, tarifa : dict)-> tuple:

SALIDAS:  return TUPLA con lista con tuplas internas
   Formato de salida= ([(id_predio,total_predio)],[consumo_menor_igual_15], [consumo_mayor_15],total)
   Ejemplo de salida= ([('501001190001', 58127.28), ('501002190324', 64291.2)], [], [72, 27], 122418.48)

'''
{} llaves
[] corchetes
() parentesis
'''

"""
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ============================= //////////////// PRUEBA No. 1
# -------------------------------------------------------------------------------
"""
# =================== DICCIONARIO 1

lectura = {
    '501001190001': {
        'toma_lectura': [
            {
                'lec_anterior': 1232,
                'lec_actual': 1304,
            }
        ],
        'estrato': 1,
        'estado': 'activo'
    },
    '501002190324': {
        'toma_lectura': [
            {
                'lec_anterior': 1203,
                'lec_actual': 1230,
            }
        ],
        'estrato': 4,
        'estado': 'activo'
    }
}
"""
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ============================= //////////////// PRUEBA No. 2
# -------------------------------------------------------------------------------
"""
lectura = {
    '501001190001': {
        'toma_lectura': [
            {
                'lec_anterior': 1232,
                'lec_actual': 1304,

            }
        ],
        'estrato': 1,
        'estado': 'inactivo'

    }
}
"""
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ============================= //////////////// PRUEBA No. 3
# -------------------------------------------------------------------------------

lectura = {
    '201501001': {
        'toma_lectura': [

            {
                'lec_anterior': 12,
                'lec_actual': 60,

            }
        ],
        'estrato': 1,
        'estado': 'activo'  # activo
    },
    '201501002': {
        'toma_lectura': [

            {
                'lec_anterior': 2,
                'lec_actual': 6,

            }
        ],
        'estrato': 2,
        'estado': 'activo'  # activo
    },
    '201501003': {
        'toma_lectura': [

            {
                'lec_anterior': 23,
                'lec_actual': 43,

            }
        ],
        'estrato': 3,
        'estado': 'activo'  # activo
    },
    '201501004': {
        'toma_lectura':
        [

            {
                'lec_anterior': 90,
                'lec_actual': 120,

            }
        ],
        'estrato': 1,
        'estado': 'activo'  # activo
    },
    '201501005': {
        'toma_lectura': [

            {
                'lec_anterior': 1,
                'lec_actual': 9,

            }
        ],
        'estrato': 1,
        'estado': 'inactivo'  # inactivo
    },
    '201564006': {
        'toma_lectura': [

            {
                'lec_anterior': 10,
                'lec_actual': 20,
            }
        ],
        'estrato': 6,
        'estado': 'activo'  # activo
    }
}

# =================== DICCIONARIO 2

tarifa = {
    'cargo_basico': 10450,
    'consumo': 1200.40
}


def inforServicio(lectura: dict, tarifa: dict) -> tuple:

    # ============================Variables basicas presupuesto
    cargo_basico = tarifa['cargo_basico']
    print("cargo basico: ", cargo_basico)
    val_consumo = tarifa['consumo']
    print("consumo: ", val_consumo)

    """ FACTORES DEPENDIENTES DEL ESTRATO:
    """
    factor1 = 0.6
    factor2 = 0.85
    factor3 = 0.9
    factor4_6 = 1.5
    factor5 = 1.5
    factor6 = 1.5
    # ====================== constitucion de variables a usar

    lista_regPredios = list()
    consumos_hogares = list()

    estado = []
    id_predios = list()

    for predio, datos in lectura.items():

        try:
            if datos["estado"] == "activo":

                id_predios.append(predio)
                print("id_predios:", id_predios)

                estado.append(datos["estado"])
                # ============================== varibles basicas diccionario lectura
                lec_anterior = datos['toma_lectura'][0]['lec_anterior']
                print("lect anterior: ", lec_anterior)
                lec_actual = datos['toma_lectura'][0]['lec_actual']
                print("lect actual: ", lec_actual)

                consumo_predio = (lec_actual) - (lec_anterior)
                print("consumo predio: ", consumo_predio)

                consumos_hogares.append(consumo_predio)
                print("consumo hogares: ", consumos_hogares)

                # ========================= COBRO REAL DE FACTURA EN DINERO
                estrato = datos['estrato']
                print("estrato: ", estrato)

                if estrato == 1:

                    total_predio = (consumo_predio*val_consumo +
                                    cargo_basico)*factor1
                    print("total consumo predio: ", total_predio)

                elif estrato == 2:

                    total_predio = (consumo_predio*val_consumo +
                                    cargo_basico)*factor2
                    print("total consumo predio: ", total_predio)

                elif estrato == 3:

                    total_predio = (consumo_predio*val_consumo +
                                    cargo_basico)*factor3
                    print("total consumo predio: ", total_predio)

                elif estrato == 4 or estrato == 5 or estrato == 6:

                    total_predio = (consumo_predio*val_consumo +
                                    cargo_basico)*factor4_6
                    print("total consumo predio: ", total_predio)

                lista_regPredios.append(round(total_predio, 2))
                print("registros consumo predios: ", lista_regPredios)

                #print("Tupla consumo predio: ", reg_predios)

        except:
            pass

    # for var in estado:
    if sum(consumos_hogares) == 0:
        return f"Sin lecturas"
    else:
        # ================ salida
        # SALIDA TUPLA CONSUMO - PREDIO
        costo_predio = zip(id_predios, lista_regPredios)
        costo_predio_final = list(costo_predio)

        # =========== Aplicacion de recurso de filter:
        menores_quin = list(filter(lambda x: x <= 15, consumos_hogares))
        print("consumos menores 15:", menores_quin)

        mayores_quin = list(filter(lambda x: x > 15, consumos_hogares))
        print("consumos menores 15:", mayores_quin)

        # ================ SALIDA FINAL ===================================
        salida_final = tuple()
        salida_final = (costo_predio_final, menores_quin,
                        mayores_quin, round(sum(lista_regPredios), 2))
        print("salida final: ", salida_final)

        return salida_final


print(inforServicio(lectura, tarifa))
