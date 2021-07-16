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

x = input("Cuantos productos ingresaras:")
x1 = int(x)


"""def ingresoProducto(prod: dict) -> str:"""


def ingresoProducto(miProducto):

    # ===================================================Parametros
    # proUtilidad (int): Utilidad del producto
    proUtilidad = 1.19

    proPrecio = proUtilidad*miProducto["proCosto"]

    # proMinstock (int): min stock del producto
    proMinstock = 10
    # proMaxstock (int): max stock del producto
    proMaxstock = 500

    # Valor total segun precio unitario
    proTotprecio = proPrecio*miProducto["proCantidad"]

    # Ajuste de variables
    proNombre = miProducto["proNombre"]
    proCodigo = miProducto["proCodigo"]

    if(miProducto["proCantidad"] > proMaxstock):
        return f"El Producto {proNombre} codigo {proCodigo} se encuentra fuera del rango max stock"

    elif(miProducto["proCantidad"] < proMinstock):
        return f"El Producto {proNombre} codigo {proCodigo} se encuentra fuera del rango min stock"

    # if(10 <= miProducto["proCantidad"] <= 500):
    else:
        return f"El producto {proNombre} codigo {proCodigo} tiene un precio {proPrecio} y su precio total es {proTotprecio} ha sido ingresado correctamente"

        # pass


if (x1 > 0):
    print("Enterado. Vamos a empezar")

    for i in range(x1):
        miProducto = {"proCodigo": input("Codigo del producto a ingresar:"),
                      "proNombre": input("Nombre del producto a ingresar:"),
                      "proCantidad": int(input("Unidades a agregar del producto:")),
                      "proCosto": float(input("Costo base del producto:"))}
        print(ingresoProducto(miProducto))
    # print(miProducto)  # Una confirmacion


"""

# “El Producto {proNombre} código {proCodigo} se encuentra fuera del rango min stock”

# “El Producto {proNombre} condigo {proCodigo} se encuentra fuera del rango max stock”

# “El producto {proNombre} codigo {proCodigo} tiene un precio {proPrecio} y su precio total es {proTotprecio} ha sido
# ingresado correctamente”

"""
