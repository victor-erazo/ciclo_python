# ejercicio ejemplo reto 5

def ejemploInf(ar: str) -> dict:

    import pandas as pd

    if ar.split('.')[1] != 'csv':
        print('ext inválida')

    try:

        df = pd.read_csv(ar, encoding='latin-1')
        df

    except:
        print('error al leer archivo')

    for columna in df.columns:
        # print(columna)
        pass

    df_filtar = df.query('TOTAL_ACTIVOS_2018 > 34000000')
    print("prueba:", df_filtar)
    df_domicilio = df_filtar[['TOTAL_ACTIVOS_2018', 'DEPARTAMENTO_DOMICILIO']]

    d_promedio = df_domicilio.groupby(
        "DEPARTAMENTO_DOMICILIO", as_index=False).mean()
    d_mediana = df_domicilio.groupby(
        "DEPARTAMENTO_DOMICILIO", as_index=False).median()
    d_totales = df_domicilio.groupby(
        "DEPARTAMENTO_DOMICILIO", as_index=False).count()

    d_datos = pd.merge(d_promedio, d_mediana, on="DEPARTAMENTO_DOMICILIO")
    d_datos = pd.merge(d_datos, d_totales, on="DEPARTAMENTO_DOMICILIO")
    d_datos.columns = ['Dpto Domicilio', 'Promedio', 'Mediana', 'Total']

    print(d_datos)

    return d_datos.to_dict


ruta = r'C:\Users\vler\Documents\10. Mintic\1.3 Ciclo1 - Fund Programacion\mision TIC 2022\grupo 09\Mision-TIC-GRUPO-09-master(16-06-21)\Semana 5\emp_1000_1.csv'

ejemploInf(ruta)
