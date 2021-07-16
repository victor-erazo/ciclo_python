"""Función para determinar montos pagados, en mora y elaborados. Reto Semana 3."""


def calcularInforme(creditos: dict) -> list:
    """Permite calcular los valores pagados, en mora y elaborados de un crédito.

    Args:
       creditos: diccionario con los argumentos requeridos.
    Returns:
       list: lista con el formato requerido para el reto de la semana 3.
    """
    salida = []
    id_cod = ''
    vlr_ven = 0
    vlr_pagado = 0
    vlr_elab = 0
    valores = ()

    for _num, usuario in enumerate(creditos):

        data_user = creditos[usuario]

        if data_user['est_credito'] == 'Pagado':

            continue

        if id_cod == '':

            id_cod = usuario
            # igual a id_cod = usuario

        else:

            id_cod = '{0}-{1}'.format(id_cod, usuario)
            # igual a id_cod += '-' + usuario

        # identificación
        ini_nombre = data_user['nombres'][0]
        ini_apellido = data_user['apellidos'][0]
        id_cod = '{0}-{1}-{2}'.format(id_cod, ini_nombre, ini_apellido)
        # igual a id_cod += ('-' + ini_nombre + '-' + ini_apellido)

        user_credit_data = data_user['credito'][0]
        cuotas = user_credit_data['cuotas']
        interes = user_credit_data['interes']
        c_ven = user_credit_data['cuo_vencidas']
        c_pagadas = user_credit_data['cuo_pagadas']
        monto = user_credit_data['valor']
        vlr_cuota = monto / cuotas
        vlr_saldo = monto
        cuota = 0

        while cuota < cuotas:

            cuota += 1
            vlr_interes = vlr_saldo * interes
            vlr_pagar = vlr_cuota + vlr_interes
            vlr_saldo -= vlr_cuota

            if cuota <= c_pagadas:

                vlr_pagado += vlr_pagar

            elif c_pagadas < cuota <= c_pagadas + c_ven:

                vlr_ven += vlr_pagar

            elif c_pagadas + c_ven < cuota <= cuotas:

                vlr_elab += vlr_pagar

        valores = (round(vlr_pagado, 2),
                   round(vlr_ven, 2),
                   round(vlr_elab, 2))

    salida.append(id_cod)
    salida.append(valores)
    return salida
