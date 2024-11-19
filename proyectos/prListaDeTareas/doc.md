[Proyectos](../index.md)

# Lista de tareas: Sistema de gestión de tareas pendientes

--- 
[Lista de tareas](https://vgonzalez165.github.io/apuntes_sge/proyectos/proyecto_ev1.html)
Crear una aplicación de consola que permita gestionar una lista de tareas.

[archivo_de_guardado](archivo.csv)

```python
import datetime
import csv

#Establecemos las variables que vamos a necesitar
finalizado = False
tareas = []

RED = '\033[31m' #color rojo
RESET = '\033[0m' # color base


#nombre del archivo de guardado
guardado = "archivo.csv"

#cargamos las tareas desde el archivo
def cargar_tareas():
    try:
        with open(guardado, mode="r", newline='', encoding="utf-8") as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                tareas.append({
                    "nombre": fila["nombre"],
                    "prioridad": fila["prioridad"],
                    "fecha_final": fila["fecha_final"],
                    "completado": fila["completado"] == "True",  # Convertir a booleano
                })
        print("Tareas cargadas correctamente.")
    except FileNotFoundError:
        print("No se encontró un archivo previo. Comenzando con una lista vacía.")
    except Exception as e:
        print(f"Error al cargar las tareas: {e}")

# Guardar tareas en el archivo CSV al salir
def guardar_tareas():
    with open(guardado, mode="w", newline='', encoding="utf-8") as archivo:
        campos = ["nombre", "prioridad", "fecha_final", "completado"]
        escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
        escritor_csv.writeheader()
        for tarea in tareas:
            escritor_csv.writerow({
                "nombre": tarea["nombre"],
                "prioridad": tarea["prioridad"],
                "fecha_final": tarea["fecha_final"],
                "completado": tarea["completado"],
            })
    print("Tareas guardadas correctamente.")

# añadimos una tarea solicitando los datos que necesitamos
def anadir_tarea():
    datos_correctos = False
    while not datos_correctos:
        print(RESET + "Introduzca los datos solicitados: ")

        # Pedimos los datos que necesitamos
        nombre = input("Introduce el nombre: " + RED)
        prioridad = input(RESET + "Introduce la prioridad de la tarea: " + RED)
        
        # Validamos la fecha
        fecha_str = input(RESET + "Introduce la fecha límite (formato DD/MM/YYYY): " + RED)
        fecha_partida = fecha_str.split("/")
        dia = int(fecha_partida[0])
        mes = int(fecha_partida[1])
        anyo = int(fecha_partida[2])
        if datetime.datetime(anyo, mes, dia):
            datos_correctos = True
    
    #se lo asignamos a la nueva tarea que introducimos
    tareas.append({
        "nombre" : nombre,
        "prioridad" : prioridad,
        "fecha_final" : fecha_str,
        "completado" : False,
    })

    print(RESET + "")
    print("Tarea añadida correctamente")

#Lista de el numero de tareas
def mostrar_lista():
    print("")
    print("Numero de tareas: " + str(len(tareas)))
    for tarea in tareas:
        print("nombre: " + tarea["nombre"])
        print("prioridad: " + tarea["prioridad"])
        print("fecha limite: " + tarea["fecha_final"])
        if(tarea["completado"]):
            print("completado: " + "si")
        else:
            print("completado: " + "no")
        print("")

#marcamos una tarea como completada usando el índice
def marcar_tarea():
    indice = input(RESET + "Selecciona el índice de la tarea: " + RED)
    if indice.isdigit() and len(tareas)-1 >= int(indice):
        if len(tareas)-1 >= int(indice):
            tarea = tareas[int(indice)]
            tarea['completado'] = True
            print(RESET + "Tarea marcada satisfactoriamente")
        else:
            print(RESET + "La tarea no se encontró")

#eliminamos la tarea que el usuario nos indique
def eliminar_tarea():
    mostrar_lista()
    indice = input(RESET + "Selecciona el índice de la tarea a eliminar: " + RED)
    if indice.isdigit() and len(tareas) > int(indice):
        tarea_eliminada = tareas.pop(int(indice))
        print(f"Tarea '{tarea_eliminada['nombre']}' eliminada correctamente.")
    else:
        print("Índice inválido.")

#código del menú:
def mostrar_menu():
    print(RESET + "1. Añadir tarea")
    print("2. Mostrar lista de tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("0. Guardar y salir")
    opcion = input("Por favor elige una opción: " + RED)
    return opcion


#cargamos el archivo
cargar_tareas()

#mientras el programa no se haya finalizado
while not finalizado:
    #llamamos a la creación del menú
    funcion = mostrar_menu()
    print("")
    if funcion == '1':
        #añadimos una tarea con las especificaciones
        anadir_tarea()
    elif funcion == '2':
        #mostramos todas las tareas de la lista
        mostrar_lista()
    elif funcion == '3':
        #marcamos tarea como completada
        marcar_tarea()
    elif funcion == '4':
        #eliminamos la tarea que le especificamos al usuario
        eliminar_tarea()
    elif funcion == '0':
        #salimos de la aplicación y guardamos
        guardar_tareas()
        finalizado = True
    else:
        #en caso de que no se haya elegido nada correcto se muestra este mensaje
        print("No has seleccionado ninguna de las opciones")
```