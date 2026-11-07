#IMPORTACIÓN DE OS Y JSON
import os
import json

#Función para validar DNI
def fn_validar_dni(dni_validar_str):

    dni_validar_str = dni_validar_str.strip().upper()

    
    if dni_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    if len(dni_validar_str) != 9:
        print("El DNI contiene 9 carácteres.")
        return False

    if not dni_validar_str[:8].isdigit():
        print("El DNI debe tener 8 dígitos")
        return False

    if not dni_validar_str[8].isalpha():
        print("El DNI debe tener una letra al final")
        return False

    return True


# OPCIÓN 1. REGISTRAR NUEVO CANDIDATO
def fn_registrar_candidato():

    dni_candidato_str = input("Introduce el DNI: ")

    while not fn_validar_dni(dni_candidato_str):

        dni_candidato_str = input("Introduce el DNI: ")

    else:
        print("DNI válido.")

#OPCIÓN 2. MODIFICAR CANDIDATO
def fn_modificar_candidato():
    print(":)")


#OPCIÓN 3. MOSTRAR TODOS LOS CANDIDATOS
def fn_mostrar_candidatos():
    print(":)")


#OPCIÓN 4. BUSCAR CANDIDATO
def fn_buscar_candidato():
    print(":)")


#OPCIÓN 5. FILTRAR CANDIDATOS
def fn_filtrar_candidatos():
    print(":)")


#OPCIÓN 6. ELIMINAR CANDIDATOS
def fn_eliminar_candidato():
    print(":)")


#OPCIÓN 7. GESTIONAR CANDIDATURAS
def fn_gestionar_candidaturas():
    print(":)")


#OPCIÓN 8. EXPORTAR INFORMES
def fn_exportar_informes():
    print(":)")


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
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

        input("\nPulsa ENTER para volver al menú principal...")

#Ejecuta el programa
fn_menu()