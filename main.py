#IMPORTACIÓN DE OS Y JSON
import os
import json

#Función para validar DNI
def fn_validar_dni(dni_validar_str):

    #Eliminar espacios del DNI y convertir la letra en mayúscula
    dni_validar_str = dni_validar_str.strip().upper()

    #Comprobar que no deja el espacio en blanco
    if dni_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    #Comprobar que el DNI tiene 9 caracteres
    if len(dni_validar_str) != 9:
        print("El DNI contiene 9 caracteres.")
        return False

    #Comprobar que los 8 primeros son números
    if not dni_validar_str[:8].isdigit():
        print("El DNI debe tener 8 dígitos.")
        return False

    #Comprobar que el último caracter es una letra
    if not dni_validar_str[8].isalpha():
        print("El DNI debe tener una letra al final.")
        return False

    return True

#Funcion limpiar y validar nombre
def fn_limpiar_nombre(nombre_validar_str):

    #Elimina espacios del nombre y convierte todo en minúsculas menos la primera letra
    nombre_validar_str = nombre_validar_str.strip().title()

    #Comprobar que no deja el espacio en blanco
    if nombre_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    #Comrpobar que el nombre solo contiene letras
    if not nombre_validar_str.replace(" ","").isalpha():
        print("El nombre solo puede contener letras.")
        return False

    return True

# OPCIÓN 1. REGISTRAR NUEVO CANDIDATO
def fn_registrar_candidato():

    #Solicitar el DNI
    dni_candidato_str = input("Introduce el DNI: ")

    #Mientras que el DNI no sea valido, repetir la funcion de validación del DNI
    while not fn_validar_dni(dni_candidato_str):

        dni_candidato_str = input("Introduce el DNI: ")

    nombre_candidato_str = input("Introduce el nombre: ")

    #Mientras que el nombre no sea correcto, repetir funcion
    while not fn_limpiar_nombre(nombre_candidato_str):
        nombre_candidato_str = input("Introduce el nombre: ")

    print("Candidato registrado correctamente.")

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