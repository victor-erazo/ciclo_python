# ejercicio ejemplo reto 5

ruta = 'C:\Users\vler\Documents\10. Mintic\1.3 Ciclo1 - Fund Programacion\mision TIC 2022\grupo 09\Mision-TIC-GRUPO-09-master(16-06-21)\Semana 5\emp_1000_1.csv'
#ruta = "emp_1000_1.csv"
# no nesecita "r" por slash en reversa
# ruta = 'C:\Usuarios\vler\Escritorio\emp_1000_1.csv'


def ejemploInf(ruta: str) -> dict:

    import pandas as pd

    if ruta.split('.')[1] != 'csv':
        print('ext inválida')

    else:
        df = pd.read_csv(ruta, encoding='latin-1')
        df
        #prueba = pd.read_csv(ruta)
        # prueba
        print(prueba)
        print("Loco se pudo")
        """
        df_filtar = df.query('TOTAL_ACTIVOS_2018 > 34000000')
        df_domicilio = df_filtar[[
            'TOTAL_ACTIVOS_2018', 'DEPARTAMENTO_DOMICILIO']]

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
        """
    # except:
     #   print('error al leer archivo')

    # for columna in df.columns:
        # print(columna)
        # pass


ejemploInf(ruta)
