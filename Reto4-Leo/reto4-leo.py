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
    # predios = []
    # consumos = []
    for predio, datos in lectura.items():

        if datos["estado"] == "activo":

            for lotes in lectura.keys():
                id_predios = lotes
                print("lotes: ", lotes)

        # ============================== varibles basicas diccionario lectura
            lec_anterior = datos['toma_lectura'][0]['lec_anterior']
            print("lect anterior: ", lec_anterior)
            lec_actual = datos['toma_lectura'][0]['lec_actual']
            print("lect actual: ", lec_actual)
            # sacar en una varible temporal codigos predios
            # id_predio = lectura.keys()
            # print("id_predio: ", id_predio)
            # saco consumo total mes en una variable temporal  en cada predio
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

            # ================ salida
            # SALIDA TUPLA CONSUMO - PREDIO
            reg_predios = (id_predios, round(total_predio, 2))
            lista_regPredios.append(reg_predios)
            # ======================================= salida
            costo_total.append(total_predio)
        print("lista_regPredios:", lista_regPredios)

        # predios.append(predio)
        # consumos.append(consumo_mes)

        # =============================== ////////  ===== Filtro de consumos
        # Considerar  funciones (filter,reduce,zip,lambda).

        """ 
        PEQUEÑO RESUMEN DE FUNCIONES MAP - FILTER - REDUCE - ZIP -LAMBDA

        1- MAP: la función map retorna un objeto map object. Objeto que 
        fácilmente podemos convertir a una lista
            Integracion LAMBDA:
            lista = [1,2,3]
            result = list ( map(lambda elemento : elemento*elemento, lista))

        2- FILTER: condicion de seleccion objetos
            Integracion LAMBDA:
            tupla = (1,2,3)
            result = tuple(filter(lamda elemento: elemento > 5, tupla))
        
        3- REDUCE: cuando poseamos una colección de elementos y necesitemos 
        generar un único resultado. nos permitirá reducir los elementos de la colección.
        Podemos ver a esta función como un acumulador. 
            Integracion LAMBDA: Ejemplo Acumulador
            result = reduce(lamda acumulador=0, elemento=0: acumulador + elemento, lista)

        4- ZIP: es una función para reorganizar listas. 
        Como parámetros admite un conjunto de listas. Lo que hace es tomar el elemento i-ésimo
        de cada lista y unirlos en una tupla, después une todas las tuplas en una sola lista.
            Integracion LAMBDA:
            nombres = ["itza","leo","maer"]
            apellidos= ["erazo","rios","lozano"]
            nom_ape= zip(nombres, apellidos)
            result = [("itza","erazo"),("leo","rios"),("maer","lozano")]

        """
        # =========== Aplicacion de recurso de filter:
        #menores_quin = []
        #menores_quin.append(filter(lambda x: x < 15, consumos_hogares))
        menores_quin = list(filter(lambda x: x <= 15, consumos_hogares))
        print("consumos menores 15:", menores_quin)

        mayores_quin = list(filter(lambda x: x > 15, consumos_hogares))
        print("consumos menores 15:", mayores_quin)

        # ================ SALIDA FINAL ===================================
        salida_final = tuple()
        salida_final = (lista_regPredios, menores_quin,
                        mayores_quin, round(sum(costo_total), 2))
        print("salida final: ", salida_final)

        # return salida_final

        if datos["estado"] == "inactivo":
            return f"Sin lecturas"

        # elif datos["estado"] == "inactivo":
        # else:
        # pass
        # return f"Sin lecturas"


print(inforServicio(lectura, tarifa))
