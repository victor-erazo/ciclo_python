# Autor YEISON CAMILO GRUPO 09

productos = {
    "proCodigo": "T00194",  # Código del producto
    "proNombre": "Televisor Smart TV",  # Nombre del producto
    "proCantidad": 50,  # Cantidad del producto
    "proCosto": 2500000  # Costo del producto
}


def ingresoProducto(productos):

    if productos['proCantidad'] < 10:
        respuesta = "El Producto " + str(productos['proNombre']) + "con el codigo " + str(
            productos['proCodigo']) + " se encuentra fuera del rango min stock"
        return(respuesta)
    elif productos['proCantidad'] > 500:
        respuesta = "El Producto " + str(productos['proNombre']) + "con el codigo " + str(
            productos['proCodigo']) + " se encuentra fuera del rango max stock"
        return(respuesta)
    else:
        porcentaje = (productos['proCosto'] * 19) / 100 + productos['proCosto']
        total = productos['proCantidad'] * productos['proCosto']

        respuesta = "El producto " + str(productos['proNombre']) + "código " + str(productos['proCodigo']) + " tiene un precio " + str(
            productos['proCosto']) + " y su precio total es " + str(total) + " ha sido ingresado correctamente \n"
        return(respuesta)


print(ingresoProducto(productos))
