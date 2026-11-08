#IMPORTACIÓN DE OS Y JSON
import os
import json

#Importar de candidatos.py las siguientes funciones
from candidatos import (
    fn_registrar_candidato,
    fn_modificar_candidato,
    fn_mostrar_candidatos,
    fn_buscar_candidato,
    fn_filtrar_candidatos,
    fn_eliminar_candidato,
    fn_gestionar_candidaturas,
    fn_exportar_informes
)

#LISTA DE CANDIDATOS
candidatos_lst = []

#FUNCIÓN PARA GUARDAR CANDIDATOS EN JSON
def fn_guardar_candidatos():

    """
    Guardar la lista de candidatos en un archivo JSON

    Almacenar los datos de candidatos_lst en candidatos.json
    """

    #Abrir archivo.json y escribir la lista de candidatos
    with open("candidatos.json", "w") as x:
        json.dump(candidatos_lst, x, indent=4)

    print("\n--- CANDIDATOS GUARDADOS CORRECTAMENTE ---")

#FUNCIÓN PARA CARGAR LOS CANDIDATOS DE JSON
def fn_cargar_candidatos():

    """
    Cargar los candidatos almacenados en el archivo JSON

    Leer el contenido de candidatos.json y cargar los datos
    para usarlos durante la ejecución del programa
    """

    #Abrir y leer el archivo.json
    with open("candidatos.json", "r") as x:

        #Todo lo que lea en el archivo.json estará en la siguiente variable
        contenido_str = x.read()

        #En caso de que el contenido este vacio creará una lista
        if contenido_str == "":
            candidatos_lst = []
        
        #Si no abrira el archivo y su contenido
        else:
            candidatos_lst = json.loads(contenido_str)

#MENÚ PRINCIPAL TALENTCONNECT
def fn_menu():

    #Bucle infinito acceder al menú hasta que se pulse la opción de salir
    while True:

        #Borrar datos de la consola
        os.system('cls')

        #Muestra las opciónes disponibles
        print("""
        -------------------------------
                TALENTCONNECT
        -------------------------------
        1. Registrar nuevo candidato
        2. Modificar candidato
        3. Mostrar todos los candidatos
        4. Buscar candidato
        5. Filtrar candidatos
        6. Eliminar candidato
        7. Gestionar candidaturas
        8. Exportar informes
        0. Guardar y salir
        -------------------------------
        """)

        opcion_seleccionada_str = input("Seleccione una opción: ")

        #Dependiendo de lo que se elija ejecutara las funciones correspondientes
        if opcion_seleccionada_str == "1":
            fn_registrar_candidato()

        elif opcion_seleccionada_str == "2":
            fn_modificar_candidato()

        elif opcion_seleccionada_str == "3":
            fn_mostrar_candidatos()

        elif opcion_seleccionada_str == "4":
            fn_buscar_candidato()

        elif opcion_seleccionada_str == "5":
            fn_filtrar_candidatos()

        elif opcion_seleccionada_str == "6":
            fn_eliminar_candidato()

        elif opcion_seleccionada_str == "7":
            fn_gestionar_candidaturas()

        elif opcion_seleccionada_str == "8":
            fn_exportar_informes()

        #Sale del bucle y del programa
        elif opcion_seleccionada_str == "0":

            fn_guardar_candidatos()

            print("\nSaliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

        input("\nPulsa ENTER para volver al menú principal...")

#Ejecuta la función con los cantitados guardados
fn_cargar_candidatos()

#Ejecuta el programa
fn_menu()