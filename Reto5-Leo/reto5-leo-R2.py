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


def infoIcfes(rt_archivo: str) -> dict:

    import pandas as pd

    if rt_archivo.split('.')[3] != 'csv':  # ALERTA AQUI....!
        print('Extensión inválida.')

    try:

        df = pd.read_csv(rt_archivo, encoding='latin-1')  # latin-1 # UTF-8
        df

    except:
        print('Error al leer el archivo de datos.')

    for columna in df.columns:
        # print(columna)
        pass
    # departamento_residencia
    # AM '17>=edad_del_estudiante>= 16'
    df_filtar = df.query('17>=edad_del_estudiante>= 16')
    df_filtar
    # print(df_filtar)
    df_domicilio = df_filtar[['edad_del_estudiante',
                              'municipio_de_residencia']]  # C
    df_domicilio
    # print(df_domicilio)

    d_promedio = df_domicilio.groupby(
        "municipio_de_residencia", as_index=False).mean()
    d_mediana = df_domicilio.groupby(
        "municipio_de_residencia", as_index=False).median()
    d_totales = df_domicilio.groupby(
        "municipio_de_residencia", as_index=False).count()

    d_datos = pd.merge(d_promedio, d_mediana, on="municipio_de_residencia")
    d_datos = pd.merge(d_datos, d_totales, on="municipio_de_residencia")
    d_datos.columns = ['Municipio', 'Promedio', 'Mediana', 'total_estudiantes']

    print(d_datos)

    return d_datos.to_dict()  # ()


#ruta = r"C:\Users\vler\Documents\10. Mintic\1.3 Ciclo1 - Fund Programacion\mision TIC 2022\grupo 09\Mision-TIC-GRUPO-09-master(16-06-21)\Pruebas_SABER_11_220_estudiantes_2020_1.csv"
ruta = r"C:\Users\vler\Documents\10. Mintic\1.3 Ciclo1 - Fund Programacion\mision TIC 2022\grupo 09\Mision-TIC-GRUPO-09-master(16-06-21)\Pruebas_SABER_11_220_estudiantes_2020_1.xlxs"


#ruta = "https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-09/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv"


"""  DIRECCION TIENE LIO DONDE DICE GRUPO  09
# ruta = r'https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO09/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv'

"""

infoIcfes(ruta)
