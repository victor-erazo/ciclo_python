def calcularInforme(creditos : dict)-> list:
    lista1=[]
    lista2=[]
    totPagados=0
    totVencidos=0
    totElaboradas=0
    
    for codigos,val in creditos.items():
        if creditos[codigos]["est_credito"] == "Activo":
            lista1="".join(str(codigos)) 
            nombre=creditos[codigos]["nombres"][0] 
            apellidos=creditos[codigos]["apellidos"][0]
            lista2+=[lista1,nombre,apellidos]
            x="-".join(lista2) 
            prestamo=creditos[codigos]["credito"][0]["valor"] 
            cuotas=creditos[codigos]["credito"][0]["cuotas"]
            vlr_cuota=prestamo/cuotas
            interes=creditos[codigos]["credito"][0]["interes"]
            cuotas_pagadas=creditos[codigos]["credito"][0]["cuo_pagadas"]
            cuo_vencidas=creditos[codigos]["credito"][0]["cuo_vencidas"]
            cuo_elaboradas=cuotas-cuotas_pagadas-cuo_vencidas
            
            
            vlr_saldo=prestamo
            for i in range(cuotas_pagadas): 
                vlr_interes=vlr_saldo*interes
                vlr_pagar=vlr_interes+vlr_cuota
                totPagados=totPagados+vlr_pagar
                vlr_saldo=vlr_saldo-vlr_cuota
            
            for j in range(cuo_vencidas): 
                vlr_interes=vlr_saldo*interes
                vlr_pagar=vlr_interes+vlr_cuota
                totVencidos=totVencidos+vlr_pagar
                vlr_saldo=vlr_saldo-vlr_cuota
            

            for y in range(cuo_elaboradas): 
                vlr_interes=vlr_saldo*interes
                vlr_pagar=vlr_interes+vlr_cuota
                cuo_elaboradas=cuotas-cuotas_pagadas-cuo_vencidas
                totElaboradas=totElaboradas+vlr_pagar
                vlr_saldo=vlr_saldo-vlr_cuota
            

    return ["-".join(lista2),(round(totPagados,2),round(totVencidos,2),round(totElaboradas,2))]