# Aplicación CRUD tareas pendientes
tareas = {
    '01':   {
                'descripcion': 'Ir al mercado',
                'estado': 'Pendiente',
                'tiempo': 60
            },
    '02':   {
                'descripcion': 'Estudiar',
                'estado': 'Pendiente',
                'tiempo': 180
            },
    '03':   {
                'descripcion': 'Hacer ejercicio',
                'estado': 'Pendiente',
                'tiempo': 50
            }
}

def menu():
    print('\n --- Aplicación CRUD Tareas Pendientes --- \n')
    print(' 1. Agregar tarea')
    print(' 2. Leer las tareas pendientes')
    print(' 3. Actualizar tarea')
    print(' 4. Eliminar tarea')
    print(' 5. Salir \n')

def crear(tareas : dict,identificador : str,nuevaTarea : dict):
    tareas[identificador] = nuevaTarea
    return tareas

def listar(tareas : dict):
    for i,info in tareas.items():
        print('Identificador -> ', i)
        for nombre_atributo,atributo in info.items():
            print(nombre_atributo,': ',atributo)
        print('\n')

def listar_d(tareas : dict):
    for i,info in tareas.items():
        print('Identificador', i ,end=' - ')
        for nombre_atributo,atributo in info.items():
            print(nombre_atributo,': ',atributo, end=', ')

def validarTarea(identificador : str,tareas : dict):
    conjuntoIdentificadores = set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False

opcion = 0
while (opcion != 5):
    menu()
    opcion = int(input('Ingrese la opción: '))
    if opcion == 1:
        print(' Agregar la tarea pendiente \n')
        identificador = str(input('ingrese el identificador de la tarea '))
        descripcion = str(input('ingresar la descripcion de la tarea '))
        estado = str(input('ingresar el estado de la tarea '))
        tiempo = int(input('ingresar el tiempo de la tarea'))
        nuevaTarea = {
            'descripcion': descripcion,
            'estado': estado,
            'tiempo': tiempo
        }
        tareas = crear(tareas,identificador,nuevaTarea)
    elif opcion == 2:
        print(' Listar las tareas pendientes \n')
        listar_d(tareas)
    elif opcion == 3:
        print(' Actualizar una tarea pendiente \n')

        identificador = str(input('Ingresar el identificador '))

        if validarTarea(identificador,tareas):
            nuevaDescripcion = input('Nueva descripcion ')
            if nuevaDescripcion:
                tareas[identificador]['descripcion'] = nuevaDescripcion
            nuevoEstado = str(input('Nuevo estado '))
            if nuevoEstado:
                tareas[identificador]['estado'] = nuevoEstado
            nuevoTiempo = input('Nuevo tiempo ')
            if nuevoTiempo:
                tareas[identificador]['tiempo'] = nuevoTiempo
        else:
            print('No ha sido encontrada la tarea ')

    elif opcion == 4:
        print(' Eliminar una tarea pendiente \n')

        identificador = input('Ingresar el identificador de la tarea para eliminar ')
        if validarTarea(identificador,tareas):
            tareas.pop(identificador)
            print('Tarea eliminada. ')
        else:
            print('No ha sido encontrada la tarea ')
else:
    print(tareas)




