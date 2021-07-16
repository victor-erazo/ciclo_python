def calcularInforme(creditos: dict) -> list:
    resultado = []

    nuevo_id = ''
    vlr_pagado = 0
    vlr_vencido = 0
    vlr_pendiente = 0

    for credito_id, persona in creditos.items():  # Solo duplas, por eso solo primera y segunda posicion del dic
        # get por que la variable est aen el for sin definir el tipo
        est_credito = persona.get('est_credito')
        if (est_credito == "Activo"):
            nuevo_id = '-'.join([nuevo_id, '-'.join([credito_id, persona.get(
                'nombres')[0], persona.get('apellidos')[0]])])  # Vacio guion ID
            for detalle_credito in persona.get('credito'):
                # Marcamos las variables antes de amortizar, son los datos con los que empezamos
                vlr_cuota = detalle_credito.get(
                    'valor')/detalle_credito.get('cuotas')
                vlr_saldo = detalle_credito.get('valor')
                for i in range(detalle_credito.get('cuotas')):
                    vlr_interes = vlr_saldo*detalle_credito.get('interes')
                    # Corren siempre, se sobreescribe el valor siempre
                    vlr_pagar = vlr_cuota+vlr_interes
                    vlr_saldo = vlr_saldo-vlr_cuota
                    if (i < detalle_credito.get('cuo_pagadas')):
                        vlr_pagado = vlr_pagado+vlr_pagar
                    # Valido los pagados, para validar los de mora, se realiza una suma de todos, pero
                    elif (i < detalle_credito.get('cuo_pagadas') + detalle_credito.get('cuo_vencidas')):
                        vlr_vencido = vlr_vencido+vlr_pagar
                    else:
                        vlr_pendiente = vlr_pendiente+vlr_pagar

    # para remover el guion de la primera posicion de la cadena
    resultado.append(nuevo_id[1:])
    resultado.append((round(vlr_pagado, 2), round(
        vlr_vencido, 2), round(vlr_pendiente, 2)))
    return resultado