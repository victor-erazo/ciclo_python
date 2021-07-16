prod = {
    'proCodigo':'T00194',
    'proNombre':'Televisor Smart TV',
    'proCantidad': 50,
    'proCosto': 2500000
}

def ingresoProducto (prod : dict)-> str:
    proNombre = prod['proNombre']
    proCodigo = prod['proCodigo']
    proUtilidad = 1.19
    proMinstock = 10
    proMaxstock = 500
    proPrecio = prod['proCosto']*proUtilidad
    proTotprecio = proPrecio*prod['proCantidad']

    #"{}-{}={}".format(var_1, var_2, rta1)    
    if prod['proCantidad'] < proMinstock:
            return ("El Producto {}  condigo {} se encuentra fuera del rango min stock".format(proNombre,proCodigo))
    elif prod['proCantidad'] > proMaxstock:
            return ("El Producto {}  condigo {} se encuentra fuera del rango max stock".format(proNombre,proCodigo))
    else:
            #return ("El producto " + prod['proNombre'] + "  código " + prod['proCodigo'] + " tiene un precio " + str(proPrecio) + " y su precio total es " + str(proTotprecio) + " ha sido ingresado correctamente")
            return ("El producto {} código {} tiene un precio {} y su precio total es {} ha sido ingresado correctamente".format(proNombre,proCodigo,proPrecio,proTotprecio))

    
print(ingresoProducto(prod))