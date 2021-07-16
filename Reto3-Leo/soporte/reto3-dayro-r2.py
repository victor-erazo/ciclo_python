def calcularInforme(creditos: dict) -> list:
    codigoUsuarios = []
    totPagadosIni = 0
    totVencidosIni = 0
    totElaboradosIni = 0
    mensaje2 = ''
    for usuarioCodigo, valores in creditos.items():
        if valores['est_credito'] != 'Pagado':
            nombre = valores['nombres'][0]  # sacar inicial del nombre
            apellido = valores['apellidos'][0]  # sacar inicial de apellido
            mensaje = usuarioCodigo + '-' + nombre + '-' + apellido
            mensaje2 += mensaje
            # Otra forma de hacer el acumulado de los codigos, con este si sale con el guion en la mitad'''mensaje = '-'.join([mensaje, '-'.join([usuarioCodigo + '-'+ nombre + '-' + apellido])])
            # print(mensaje)'''
            cuotaBase = valores['credito'][0]['valor'] / \
                valores['credito'][0]['cuotas']  # definir cuota base # definir cuota interes
            intereses = valores['credito'][0]['valor'] * \
                valores['credito'][0]['interes']
            cuotaAPagar = cuotaBase + intereses
            valorTotalactivo = valores['credito'][0]['valor']
            n_cuotas = valores['credito'][0]['cuotas']

            # valores variables vvv
            for operaciones in range(n_cuotas):
                interesActivo = valorTotalactivo * \
                    valores['credito'][0]['interes']
                print("interes activo: ", interesActivo)
                valorTotalactivo -= cuotaBase
                cuotaAPagarActivo = cuotaBase + interesActivo

                if operaciones < valores['credito'][0]['cuo_pagadas']:
                    totPagadosIni += cuotaAPagarActivo
                if operaciones >= valores['credito'][0]['cuo_pagadas'] and operaciones < (valores['credito'][0]['cuo_pagadas'] + valores['credito'][0]['cuo_vencidas']):
                    totVencidosIni += cuotaAPagarActivo
                if operaciones >= (valores['credito'][0]['cuo_pagadas'] + valores['credito'][0]['cuo_vencidas']):
                    totElaboradosIni += cuotaAPagarActivo
    tuplita = (round(totPagadosIni, 2), round(
        totVencidosIni, 2), round(totElaboradosIni, 2))
    codigoUsuarios.append(mensaje2)
    codigoUsuarios.append(tuplita)
    return codigoUsuarios


'''credito = {'2015020192098': {
    'nombres': 'Juan',
    'apellidos': 'AriasRuiz',
    'est_credito': 'Activo',
    'credito': [
        {
            'id_credito': 'C0198238',
            'cuotas': 24,
            'valor': 3066936.00,
            'interes': 0.020,
            'cuo_vencidas': 8,
            'cuo_pagadas': 10}
    ]
}
}
'''
creditos = {
    "2018015647382": {
        "nombres": "Luis Antonio",
        "apellidos": "Lopez Rueda",
        "est_credito": "Activo",
        "credito": [
            {
                "id_credito": "C0013453",
                "cuotas": 60,
                "valor": 87558500,
                "interes": 0.020,
                "cuo_vencidas": 30,
                "cuo_pagadas": 7
            }
        ]
    },
    "2019041209845": {
        "nombres": "Elias",
        "apellidos": "Diaz Lopez",
        "est_credito": "Activo",
        "credito": [
            {
                "id_credito": "C0335501",
                "cuotas": 3,
                "valor": 87558,
                "interes": 0.020,
                "cuo_vencidas": 1,
                "cuo_pagadas": 2
            }
        ]
    },
    '2015020192098': {
        'nombres': 'Juan',
        'apellidos': 'Arias Ruiz',
        'est_credito': 'Activo',
        'credito': [
            {
                'id_credito': 'C0198238',
                'cuotas': 24,
                'valor': 3066936.00,
                'interes': 0.020,
                'cuo_vencidas': 8,
                'cuo_pagadas': 10
            }
        ]
    }
}

calcularInforme(creditos)
print(calcularInforme(creditos))
