"""
Desarrollo de reto # 4
Victor Leandro Erazo Rios - Grupo 09
------------------------------------------------------------------------------

INPUT:  
https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO09/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv.


PROCESADOR (Funcion):  obtener el Promedio,
                        def infoIcfes(rt_archivo: str)-> dict:


SALIDAS:  
Mensaje Correcto
{'Municipio': {municipio_de_residencia}, 'Promedio': {df_promedio }, 'Mediana': {df_mediana}, 'Total
Estudiantes': {df_totales}}

Mensaje cuando la extensión es inválida
“Extensión inválida.”

Mensaje cuando el link del archivo o nombre de archivo es incorrecto
“Error al leer el archivo de datos.”

'''
{} llaves
[] corchetes
() parentesis
'''

"""

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ============================= //////////////// PRUEBA No. 1
# -------------------------------------------------------------------------------

rt_archivo = 'https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO09/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv'

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ============================= //////////////// PRUEBA No. 2
# -------------------------------------------------------------------------------

"""
rt_archivo = r"https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-09/master/Pruebas_SABER_11_220_estudiantes_2020_1.xlxs"
"""

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ============================= //////////////// PRUEBA No. 3
# -------------------------------------------------------------------------------
"""
rt_archivo = r"https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-09/master/Pruebas_SABER_11_220_estudiantes_202.csv"
"""

# Pruebas_SABER_11_220_estudiantes_2020_1.csv

# rt_archivo = 'C:\Usuarios\vler\Escritorio\Pruebas_SABER_11_220_estudiantes_2020_1.csv'
#rt_archivo = r'C:\Usuarios\vler\Escritorio\Pruebas_SABER_11_220_estudiantes_2020_1.csv'


def infoIcfes(rt_archivo: str) -> dict:

    import pandas as pd

    if rt_archivo.split('.')[3] != 'csv':
        print('Extensión inválida.')

    # else:
    #    print("ponete pilas mk")

    # elif rt_archivo.split('.')[3] == 'csv':
    else:  # Para tener salidas unicas, deberia existir este
        try:
            df = pd.read_csv(rt_archivo, encoding='latin-1')
            df
            #df = pd.read_csv(rt_archivo)
            # print(df)
            print("lectura bien")
        except:
            print('Error al leer el archivo de datos.')


infoIcfes(rt_archivo)
