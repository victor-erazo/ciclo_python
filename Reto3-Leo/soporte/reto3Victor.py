def calcularInforme(credito):
    codigos=list(credito.keys())
    pagadas=0
    enMora=0
    elaboradas=0
    info=[]
    for codigo in codigos:
        if credito[codigo]['est_credito']!='Pagado':
            vlr_cuota=credito[codigo]['credito'][0]['valor']/credito[codigo]['credito'][0]['cuotas']
            saldo=credito[codigo]['credito'][0]['valor']
            info.append(codigo+'-'+credito[codigo]['nombres'][0]+'-'+credito[codigo]['apellidos'][0])
            for i in range(credito[codigo]['credito'][0]['cuotas']):
                vlr_interes=saldo*credito[codigo]['credito'][0]['interes']
                vlr_pagar=vlr_cuota+vlr_interes
                saldo-=vlr_cuota
                if i<credito[codigo]['credito'][0]['cuo_pagadas']:
                    pagadas+=vlr_pagar
                if credito[codigo]['credito'][0]['cuo_pagadas']<=i<credito[codigo]['credito'][0]['cuo_pagadas']+credito[codigo]['credito'][0]['cuo_vencidas']:
                    enMora+=vlr_pagar
                if i>=credito[codigo]['credito'][0]['cuo_pagadas']+credito[codigo]['credito'][0]['cuo_vencidas']:
                    elaboradas+=vlr_pagar
    pagadas=round(pagadas,2)
    enMora=round(enMora,2)
    elaboradas=round(elaboradas,2)
    return ['-'.join(info),(pagadas,enMora,elaboradas)]