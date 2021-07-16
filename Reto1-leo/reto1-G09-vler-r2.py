"""
==========================================================================

Fecha: 04/05/2021
Universidad: Tecnologica de Pereira
Materia: Fundamentos de Programacion - Grupo 09

-------------- RETO # 1 MINTIC -------------------------------------------

Nombre: Victor Leandro Erazo Rios
C.C:1.130.629.991
============================================================================
"""
# ========================================Definicion de Diccionario


"""def ingresoProducto(prod: dict) -> str:"""


def ingresoProducto(prod: dict) -> str:

    # ===================================================Parametros
    # proUtilidad (int): Utilidad del producto
    proUtilidad = 1.19
    print(type(proUtilidad))  # Ojooooooooooooooooo!!!

    proPrecio = proUtilidad*producto["proCosto"]

    # proMinstock (int): min stock del producto
    proMinstock = 10
    # proMaxstock (int): max stock del producto
    proMaxstock = 500

    # Valor total segun precio unitario
    proTotprecio = proPrecio*producto["proCantidad"]

    # Ajuste de variables
    proNombre = producto["proNombre"]
    proCodigo = producto["proCodigo"]

    if(producto["proCantidad"] > proMaxstock):
        return f"El Producto {proNombre}  código {proCodigo} se encuentra fuera del rango max stock"

    elif(producto["proCantidad"] < proMinstock):
        return f"El Producto {proNombre}  código {proCodigo} se encuentra fuera del rango min stock"

    else:
        return f"El producto {proNombre}  código {proCodigo} tiene un precio {proPrecio} y su precio total es {proTotprecio} ha sido ingresado correctamente"


producto = {"proCodigo": "T00194",
            "proNombre": "Televisor Smart TV",
            "proCantidad": int(50),
            "proCosto": 2500000}

print(ingresoProducto(producto))
