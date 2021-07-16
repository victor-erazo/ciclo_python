import time , os
from tabulate import tabulate


### Esto es la presentación del programa.
os.system('cls')
auditor=input("Ingrese nombre: ")
os.system('cls')
print(f"Cordial saludo {auditor}. \n","\n"
"El siguiente programa cumple la función de auditar el inventario de nuevos artículos de electrodomésticos, \n",
"según la utilidad que estos han presentado a la compañía. Es importante que se ingresen los datos de forma \n",
"precisa y siguiendo las indicaciones que se exponen en la terminal. \n",
"Tener a la mano los datos de: Código del Producto, Nombre del Producto, Cantidad del Producto y Costo. \n")
time.sleep(10)
os.system('cls')


datos = {
    'Código'     : [],
    'Nombre'     : [],
    'Cantidad'   : [],
    'Costo'      : [],
    'Utilidad'   : [],
    'Comentario' : []
 } #Esto es para crear el diccionario que guarda los datos de los artículos pedidos para auditoría.

# Función para calcular las utilidades y dar las respuestas según la cantidad de artículos a auditar
def PedirDatos(proCod, proNom, proCan, proCos):
    proUti = int(proCan)*int(proCos)*1.19  # Esto calcula la utilidad aprovechando la propiedad distributiva en anillo de los reales 
    if (int(proCan) >= 10 and int(proCan) <= 500): # Esto es la prueba del si 10 =< cantidad <= 500
        #Uso la función AND para enlazar ambas solicitures
        msg = f"El producto {proNom} código {proCod} \ntiene un precio {proCos} y su Precio \nLote Total \nes {proUti} ha sido ingresado \ncorrectamente"
    else: # Esta es la función del caso falso para el if de arriba
        msg = f"El producto {proNom} código {proCod} \nestá por fuera del rango de producto \ndefinido (Min:10 - Max:500)"
    #Esto guarda los valores en el diccionario creado arriba
    datos['Código'].append(proCod)
    datos['Nombre'].append(proNom)
    datos['Cantidad'].append(proCan)
    datos['Costo'].append(proCos)
    datos['Utilidad'].append(proUti)
    datos['Comentario'].append(msg)
    return print(msg)


def recurrencia(): # Esta función pide los 5 artículos de manera recurrente
    a = 1
    
    while a < 6: #La función while con su prueba de: mientras la variable a sea menor que el 6 
    ### Acá pido los valores de cada artículo a auditar
        print(f"Ingrese los datos para el artículo {a}")
        cod = input('Ingrese Código Producto: ')
        nom = input('Ingrese Nombre Producto: ')
        can = int(input('Ingrese cantidad Producto: '))
        cos = int(input('Ingrese Costo Producto: '))
    ### Acá los mando a la función que se definió arriba
        PedirDatos(cod, nom, can, cos)
    ### Esto hace que aumente el valor de a para recibir los datos según se dice en la prueba del While
        a+= 1
        time.sleep(2)  # Esto es un toque para dar tiempo de espera entre un  artículo y otro
        os.system('cls') # Esto límpia la pantalla para que no se monte un artículo sobre otro


recurrencia()
print(tabulate(datos, headers='keys',tablefmt="pipe"))
print(f"Auditado por {auditor}")
