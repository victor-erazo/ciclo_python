def calcularInforme(creditos: dict) -> list:
    total_pagadas = 0
    total_vencidas = 0
    total_elaboradas = 0
    mensaje2 = ""
    lista_salida = []

    # sacar id e iniciales de los nombres...
    for llave, valores in creditos.items():

        # solo entran creditos cuyo estado es activo
        if valores["est_credito"] == "Activo":

            # inicial del nombre
            inicial_nombre = valores["nombres"][0]
            # inicial del apellido
            inicial_apellido = valores["apellidos"][0]

            # valor total del credito
            monto = valores["credito"][0]["valor"]
            # numero de cuotas
            no_cuotas = valores["credito"][0]["cuotas"]
            # cuota fija
            vlr_cuota = (monto / no_cuotas)
            # los intereses
            interes = valores["credito"][0]["interes"]
            # cuotas ya pagas
            cuotas_pagas = valores["credito"][0]["cuo_pagadas"]
            # cuotas vencidas
            cuota_vencida = valores["credito"][0]["cuo_vencidas"]

            mensaje = llave+"-"+inicial_nombre+"-"+inicial_apellido + \
                "-"  # cadena con los codigos y las iniciales
            mensaje2 += mensaje

            # ciclo hasta el numero de cuotas
            for x in range(no_cuotas):
                # valor a pagar valos total mas los intereses
                vlr_pagar = monto * interes
                # valor total menos valor a pagar cada vuelta se decrementa
                monto -= vlr_cuota
                cta = vlr_cuota + vlr_pagar  # valor de la cuota fija mas valor a pagar

                if x < cuotas_pagas:
                    total_pagadas += cta
                if x >= cuotas_pagas and x < cuotas_pagas + cuota_vencida:
                    total_vencidas += cta
                if x >= cuotas_pagas + cuota_vencida:
                    total_elaboradas += cta

    mensaje_tupla = (round(total_pagadas, 2), round(
        total_vencidas, 2), round(total_elaboradas, 2))
    # añadircadena a la lista de salida
    lista_salida.append(mensaje2[:-1])
    lista_salida.append(mensaje_tupla)

    return(lista_salida)
