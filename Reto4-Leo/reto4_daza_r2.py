# Reto No 4 Andres Daza Rivera

from functools import reduce
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
# Diccionarios tarifa:
tarifa = dict()
tarifa['cargo_basico'] = 10450
tarifa['consumo'] = 1200.40


def inforServicio(dicc_lectura, dicc_tarifa):  # ================= inquietud
    # Subsidios y contribuciones (0.6 = 1-0.4)
    subsidios = [('1', 0.6), ('2', 0.85), ('3', 0.9),
                 ('4', 1.5), ('5', 1.5), ('6', 1.5)]
    # Variables respuesta
    id_predio = []
    total_predio = 0
    metros = []
    estratos = []

    for idPre, infPre in dicc_lectura.items():
        for infEsp in infPre['toma_lectura']:

            try:

                if infPre['estado'] == 'activo':
                    id_predio.append(idPre)
                    estratos.append(infPre['estrato'])
                    metros.append(infEsp['lec_actual'] -
                                  infEsp['lec_anterior'])
            except:
                pass
    consumo_menor_igual_15 = list(filter(lambda item: item <= 15, metros))
    consumo_mayor_15 = list(filter(lambda item: item > 15, metros))
    val_consumo = list(map(lambda x: x*tarifa['consumo'], metros))
    val_cargo_fijo = list(map(lambda x: 1*tarifa['cargo_basico'], metros))
    # volver c/u de los estratos en cadena
    estrato_str = list(map(str, estratos))
    cvar_Est = list((zip(estrato_str, val_consumo)))
    cfijo_Est = list((zip(estrato_str, val_cargo_fijo)))

    def totales_Predio(lista1, lista2):  # ============================ inquietud
        lista_resultado = []
        for x in lista1:  # lista tuplas valores-estrato
            for p, y in enumerate(lista2):  # lista con tuplas estrato-subsidio
                if x[0] in lista2[p]:
                    lista_resultado.append(x[1]*y[1])

        # print("prueba1", lista1)
        # print("prueba2", lista2)
        # print("prueba", lista_resultado)

        return lista_resultado

    valor_1 = totales_Predio(cfijo_Est, subsidios)
    valor_2 = totales_Predio(cvar_Est, subsidios)
    valor_predios = list(map(lambda x, y: round(x+y, 2), valor_1, valor_2))
    #print("prueba loca:", valor_predios)

    total_predio = sum(valor_predios)
    # total_predio = reduce(lambda x, acum=0.00000000000001: (acum + x),
    # valor_predios)  # ============== inquietud
    resultado_parcial = list()

    for x, y in zip(id_predio, valor_predios):
        resultado_parcial.append((x, y))
    # print("result parcial:", resultado_parcial)

    if total_predio == 0:
        return f"Sin Lecturas"
    else:

        resultado_final = resultado_parcial, consumo_menor_igual_15, consumo_mayor_15, total_predio
        return resultado_final
    # lectura.pop('201501005')
    # lectura.pop('501001190001')
    # return resultado_final


print(inforServicio(lectura, tarifa))
