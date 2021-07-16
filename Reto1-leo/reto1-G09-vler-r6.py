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
# cODIGO LIMPIO PARA EVALUADOR


def ingresoProducto(prod: dict) -> str:

    # ===================================================Parametros
    # proUtilidad (int): Utilidad del producto
    proUtilidad = 19

    proPrecio = prod["proCosto"]+(proUtilidad*prod["proCosto"]/100)

    # proMinstock (int): min stock del producto
    proMinstock = 10
    # proMaxstock (int): max stock del producto
    proMaxstock = 500

    # Valor total segun precio unitario
    proTotprecio = proPrecio*prod["proCantidad"]

    # Ajuste de variables
    proNombre = prod["proNombre"]
    proCodigo = prod["proCodigo"]

    if(prod["proCantidad"] > proMaxstock):
        return f"El Producto {proNombre} condigo {proCodigo} se encuentra fuera del rango max stock"

    elif(prod["proCantidad"] < proMinstock):
        return f"El Producto {proNombre} condigo {proCodigo} se encuentra fuera del rango min stock"

    else:
        return f"El producto {proNombre}  código {proCodigo} tiene un precio {proPrecio} y su precio total es {proTotprecio} ha sido ingresado correctamente"
