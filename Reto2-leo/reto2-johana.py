def calcular_seguro(datos_cliente: dict) -> dict:

    if (datos_cliente["edad"] <= 24):
        valorseguro = 0.15 * datos_cliente["val_asegurado"]

        if (datos_cliente["tipo_seguro"]) == "TERREMOTO" or (datos_cliente["tipo_seguro"]) == "INCENDIO":
            valorseguro = valorseguro - (valorseguro * 0.5)

        else:
            # if (datos_cliente["tipo_seguro"])== "SALUD" or (datos_cliente["tipo_seguro"])=="VIDA" :
            valorseguro = valorseguro - (valorseguro * 0.10)

    elif (datos_cliente["edad"] >= 25 and (datos_cliente["edad"] <= 49)):
        # if (datos_cliente["edad"] >= 25 and (datos_cliente["edad"] <= 49)):
        valorseguro = 0.20 * (datos_cliente["val_asegurado"])

        if (datos_cliente["tipo_seguro"]) == "TERREMOTO" or (datos_cliente["tipo_seguro"]) == "INCENDIO":
            valorseguro = valorseguro - (valorseguro * 0.5)

        else:
            # if (datos_cliente["tipo_seguro"])== "SALUD" or (datos_cliente["tipo_seguro"])=="VIDA" :
            valorseguro = valorseguro - (valorseguro * 0.10)

    else:
        # if (datos_cliente["edad"]>=50):
        valorseguro = 0.25 * datos_cliente["val_asegurado"]

        if (datos_cliente["tipo_seguro"]) == "TERREMOTO" or (datos_cliente["tipo_seguro"]) == "INCENDIO":
            valorseguro = valorseguro - (valorseguro * 0.5)

        else:
            # if (datos_cliente["tipo_seguro"])== "SALUD" or (datos_cliente["tipo_seguro"])=="VIDA" :
            valorseguro = valorseguro - (valorseguro * 0.10)

    dicSalida = {"nombreCompleto": datos_cliente["nombre"],
                 "tipo": datos_cliente["tipo_seguro"],
                 "valor": round(valorseguro)}

    return "El valor del seguro de {tipo} de {nombreCompleto} es: {valor}, incluyendo la promoción del mes".format(**dicSalida)


datos_cliente = {"nombre": "Pedro Díaz",
                 "tipo_seguro": "SALUD",
                 "edad": int(24),
                 "val_asegurado": int(10000000)}

print(calcular_seguro(datos_cliente))
