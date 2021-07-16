""" 
            PEQUEÑO RESUMEN DE FUNCIONES MAP - FILTER - REDUCE - ZIP -LAMBDA

            1- MAP: la función map retorna un objeto map object. Objeto que 
            fácilmente podemos convertir a una lista
                Integracion LAMBDA:
                lista = [1,2,3]
                result = list ( map(lambda elemento : elemento*elemento, lista))

            2- FILTER: condicion de seleccion objetos
                Integracion LAMBDA:
                tupla = (1,2,3)
                result = tuple(filter(lambda elemento: elemento > 5, tupla))
            
            3- REDUCE: cuando poseamos una colección de elementos y necesitemos 
            generar un único resultado. nos permitirá reducir los elementos de la colección.
            Podemos ver a esta función como un acumulador. 
                Integracion LAMBDA: Ejemplo Acumulador
                result = reduce(lamda acumulador=0, elemento=0: acumulador + elemento, lista)

            4- ZIP: es una función para reorganizar listas. 
            Como parámetros admite un conjunto de listas. Lo que hace es tomar el elemento i-ésimo
            de cada lista y unirlos en una tupla, después une todas las tuplas en una sola lista.
                Integracion LAMBDA:
                nombres = ["itza","leo","maer"]
                apellidos= ["erazo","rios","lozano"]
                nom_ape= zip(nombres, apellidos)
                result = [("itza","erazo"),("leo","rios"),("maer","lozano")]

            """
