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
        'estado': 'activo'
    },
    '201501002': {
        'toma_lectura': [

            {
                'lec_anterior': 2,
                'lec_actual': 6,

            }
        ],
        'estrato': 2,
        'estado': 'activo'
    },
    '201501003': {
        'toma_lectura': [

            {
                'lec_anterior': 23,
                'lec_actual': 43,

            }
        ],
        'estrato': 3,
        'estado': 'activo'
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
        'estado': 'activo'
    },
    '201501005': {
        'toma_lectura': [

            {
                'lec_anterior': 1,
                'lec_actual': 9,

            }
        ],
        'estrato': 1,
        'estado': 'inactivo'
    },
    '201564006': {
        'toma_lectura': [

            {
                'lec_anterior': 10,
                'lec_actual': 20,
            }
        ],
        'estrato': 6,
        'estado': 'activo'
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
    reg_predios = tuple()
    lista_regPredios = list()
    consumos_hogares = list()
    costo_total = []
    estado = []
    id_predios = list()
    # predios = []
    # consumos = []
    for predio, datos in lectura.items():
        # datos["estado"]=
        estado.append(datos["estado"])
    print("salida estado predios: ", estado)

       if any(estado) == "activo":
            print("Listo papa")

        else:
            print("chao loco")


print(inforServicio(lectura, tarifa))
