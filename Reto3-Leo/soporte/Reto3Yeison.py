# autor Yeison Camilo grupo 09 mision tic 2022
 

def calcularInforme(creditos : dict)-> list:
    total_pagadas    = 0
    total_vencidas   = 0
    total_elaboradas = 0
    mensaje2         = ""
    lista_salida     = []

    for llave, valores in creditos.items():                             # sacar id e iniciales de los nombres...

        if valores["est_credito"] == "Activo":                          # solo entran creditos cuyo estado es activo

            inicial_nombre    = valores["nombres"][0]                   # inicial del nombre
            inicial_apellido  = valores["apellidos"][0]                 # inicial del apellido 
        
            monto         = valores["credito"][0]["valor"]              # valor total del credito
            no_cuotas     = valores["credito"][0]["cuotas"]             # numero de cuotas
            vlr_cuota     = (monto / no_cuotas)                         # cuota fija
            interes       = valores["credito"][0]["interes"]            # los intereses
            cuotas_pagas  = valores["credito"][0]["cuo_pagadas"]        # cuotas ya pagas
            cuota_vencida = valores["credito"][0]["cuo_vencidas"]       # cuotas vencidas 

            mensaje = llave+"-"+inicial_nombre+"-"+inicial_apellido+"-" # cadena con los codigos y las iniciales
            mensaje2+=mensaje

            for x in range(no_cuotas):                                  # ciclo hasta el numero de cuotas
                vlr_pagar = monto * interes                             # valor a pagar valos total mas los intereses
                monto -= vlr_cuota                                      # valor total menos valor a pagar cada vuelta se decrementa
                cta = vlr_cuota + vlr_pagar                             #  valor de la cuota fija mas valor a pagar 

                if x < cuotas_pagas :
                    total_pagadas += cta
                if x >= cuotas_pagas and x < cuotas_pagas + cuota_vencida :
                    total_vencidas += cta
                if x >= cuotas_pagas + cuota_vencida:
                    total_elaboradas += cta
            
        

    mensaje_tupla = (round(total_pagadas,2),round(total_vencidas,2),round(total_elaboradas,2))
    lista_salida.append(mensaje2[:-1])                                # añadircadena a la lista de salida
    lista_salida.append(mensaje_tupla)
        
    return(lista_salida)