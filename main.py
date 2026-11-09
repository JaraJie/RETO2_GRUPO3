#IMPORTAR OS - JARA
import os

#IMPORTACIÓN DE ALMACENAMIENTO - JARA
from almacenamiento import (
    candidatos_lst,
    fn_guardar_candidatos,
    fn_cargar_candidatos
)

#IMPORTACIÓN DE FUNCIONES DE CANDIDATOS - JARA
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

#MENÚ PRINCIPAL TALENTCONNECT - JARA
def fn_menu():

    """
    Muestra el menú principal de TalentConnect

    Permite acceder a las diferentes funcionalidades
    del programa, ejecuta la opción seleccionada que
    llama a la funcíon correspondiente
    """

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

#Ejecuta la función con los cantitados guardados - JARA
candidatos_lst = fn_cargar_candidatos(candidatos_lst)

#Ejecuta el programa - JARA
fn_menu()