# creación de archivos txt

ruta = r'C:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\ciclo_uno\GRUPO_09\Semana 5\archivo.txt'


# Crea o escritura el archivo txt
fichero = open(ruta,'w')

# Agregar información al final del archivo txt
fichero = open(ruta, 'a')

# solo lectura del un archivo txt
fichero = open(ruta,'r')

fichero.close()