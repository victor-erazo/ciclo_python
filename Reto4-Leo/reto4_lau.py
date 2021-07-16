def inforServicio(lectura: dict, tarifa: dict) -> tuple:
    from functools import reduce
    # lecturas_activas = [(id, det_lectura) for id, det_lectura in lectura.items() if det_lectura['estado'] == 'activo']
    lecturas_activas = list(filter(
        lambda tupla_lectura: tupla_lectura[1]['estado'] == 'activo', lectura.items()))
    # print(lecturas_activas)
    if (len(lecturas_activas) <= 0):
        return 'Sin lecturas'

    # lecturas_activas = lectura.items()

    def func_obtener_valor(valor, key):
        if type(valor) == tuple:
            valor = valor[1]

        if type(valor) != float:
            # print(valor[key])
            return valor[key]
        return valor

    def func_lectura_consumo(tupla_lectura):
        tasa_sub_con = 0.5
        if (tupla_lectura[1]['estrato'] == 1):
            tasa_sub_con = 1 - 0.4
        elif (tupla_lectura[1]['estrato'] == 2):
            tasa_sub_con = 1 - 0.15
        elif (tupla_lectura[1]['estrato'] == 3):
            tasa_sub_con = 1 - 0.1
        else:
            tasa_sub_con = tasa_sub_con + 1

        total_lec_anterior = reduce(lambda lec1, lec2: func_obtener_valor(
            lec1, 'lec_anterior') + func_obtener_valor(lec2, 'lec_anterior'),  tupla_lectura[1]['toma_lectura'], 0.0)
        total_lec_actual = reduce(lambda lec1, lec2: func_obtener_valor(
            lec1, 'lec_actual') + func_obtener_valor(lec2, 'lec_actual'),  tupla_lectura[1]['toma_lectura'], 0.0)
        total_lecturas = (int(total_lec_actual) - int(total_lec_anterior))
        tupla_lectura[1]['cosumo'] = total_lecturas
        tupla_lectura[1]['total_predio'] = round(
            ((tarifa['cargo_basico'] * tasa_sub_con) + (tarifa['consumo'] * total_lecturas * tasa_sub_con)), 2)

        return tupla_lectura
    lectura_consumo = list(map(func_lectura_consumo, lecturas_activas))
    # print(lectura_consumo)
    # (id_predio,total_predio)
    id_totales = list(map(lambda tupla_lectura: (
        tupla_lectura[0], tupla_lectura[1]['total_predio']), lectura_consumo))
    # [consumo_menor_igual_15]
    consumo_menor_igual_15 = list(map(lambda tupla_lectura: tupla_lectura[1]['cosumo'], filter(
        lambda tupla_lectura: tupla_lectura[1]['cosumo'] <= 15, lectura_consumo)))
    # consumo_mayor_15
    consumo_mayor_15 = list(map(lambda tupla_lectura: tupla_lectura[1]['cosumo'], filter(
        lambda tupla_lectura: tupla_lectura[1]['cosumo'] > 15, lectura_consumo)))
    # total
    total = reduce(lambda tupla_lectura1, tupla_lectura2: func_obtener_valor(
        tupla_lectura1, 'total_predio') + func_obtener_valor(tupla_lectura2, 'total_predio'), lectura_consumo)
    # total=reduce(lambda tupla_lectura1, tupla_lectura2: print(func_obtener_valor(tupla_lectura2[1], 'total_predio')), lectura_consumo)
    return (id_totales, consumo_menor_igual_15, consumo_mayor_15, total)
