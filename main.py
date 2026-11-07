#IMPORTACIÓN DE OS Y JSON
import os
import json

#Función para validar DNI
def fn_validar_dni(dni_validar_str):

    #Eliminar espacios (inicio/final) y convertir la letra en mayúscula
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

    return dni_validar_str

#Función limpiar y validar nombre
def fn_limpiar_nombre(nombre_validar_str):

    #Elimina espacios (inicio/final) y convierte todo en minúsculas menos la primera letra de cada palabra
    nombre_validar_str = nombre_validar_str.strip().title()

    #Comprobar que no deja el espacio en blanco
    if nombre_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    #Comprobar que el nombre solo contiene letras, permitiendo espacios para los nombres compuestos
    if not nombre_validar_str.replace(" ","").isalpha():
        print("El nombre solo puede contener letras.")
        return False

    return nombre_validar_str


#Función limpiar y validar apellidos
def fn_limpiar_apellidos(apellidos_validar_str):

    #Elimina espacios (inicio/final) y convierte todo en minúsculas menos la primera letra de cada palabra
    apellidos_validar_str = apellidos_validar_str.strip().title()

    #Comprobar que no deja el espacio en blanco
    if apellidos_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    #Comprobar que los apellidos solo contienen letras, permitiendo espacios
    if not apellidos_validar_str.replace(" ","").isalpha():
        print("Los apellidos solo puede contener letras.")
        return False

    return apellidos_validar_str

#Función para validar edad
def fn_validar_edad (edad_validar_str):

    #Eliminar espacios (inicio/final)
    edad_validar_str = edad_validar_str.strip()

    #Comprobar que no deja el espacio en blanco
    if edad_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    #Comprobar que es un número
    if not edad_validar_str.isdigit():
        print("La edad debe ser un número entero y positivo.")
        return False

    #Convertir la edad de texto a número
    edad_validar_int = int(edad_validar_str)

    #Comprobar que sea mayor de 18 años
    if edad_validar_int < 18:
        print("El candidato debe tener al menos 18 años.")
        return False

    return edad_validar_int

#Función para limpiar y validar ciudad
def fn_limpiar_ciudad(ciudad_validar_str):

    #Elimina espacios (inicio/final) y convierte todo en minúsculas menos la primera letra de cada palabra
    ciudad_validar_str = ciudad_validar_str.strip().title()

    #Comprobar que no deja el espacio en blanco
    if ciudad_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    #Comprobar que los apellidos solo contienen letras, permitiendo espacios y guiones
    if not ciudad_validar_str.replace(" ","").replace("-","").isalpha():
        print("La ciudad solo puede contener letras.")
        return False

    return ciudad_validar_str

# OPCIÓN 1. REGISTRAR NUEVO CANDIDATO
def fn_registrar_candidato():

    #SOLICITAR DNI DEL CANDIDATO
    dni_candidato_str = input("Introduce el DNI: ")

    dni_candidato_str = fn_validar_dni(dni_candidato_str)

    #Mientras que el DNI no sea valido, repetir la funcion de validación del DNI
    while dni_candidato_str == False:
        dni_candidato_str = input("Introduce el DNI: ")
        dni_candidato_str = fn_validar_dni(dni_candidato_str)

    #SOLICITAR NOMBRE DEL CANDIDATO
    nombre_candidato_str = input("Introduce el nombre: ")

    #Llama a la función nombre y guarda el resultado en la variable
    nombre_candidato_str = fn_limpiar_nombre(nombre_candidato_str)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while nombre_candidato_str == False:
        nombre_candidato_str = input("Introduce el nombre: ")
        nombre_candidato_str = fn_limpiar_nombre(nombre_candidato_str)

    #SOLICITAR APELLIDOS DEL CANDIDATO
    apellidos_candidato_str = input("Introduce los apellidos: ")

    #Llama a la función apellidos y guarda el resultado en la variable
    apellidos_candidato_str = fn_limpiar_apellidos(apellidos_candidato_str)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while apellidos_candidato_str == False:
        apellidos_candidato_str = input("Introduce los apellidos: ")
        apellidos_candidato_str = fn_limpiar_apellidos(apellidos_candidato_str)

    #SOLICITAD EDAD DEL CANDIDATO
    edad_candidato_int = input("Introduce la edad: ")

    #Llama a la función edad y guarda el resultado en la variable
    edad_candidato_int = fn_validar_edad(edad_candidato_int)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while edad_candidato_int == False:
        edad_candidato_int = input("Introduce la edad: ")
        edad_candidato_int = fn_validar_edad(edad_candidato_int)

    #SOLICITAR CIUDAD DEL CANDIDATO
    ciudad_candidato_str = input("Introduce la ciudad: ")

    #Llama a la función ciudad y guarda el resultado en la variable
    ciudad_candidato_str = fn_limpiar_ciudad(ciudad_candidato_str)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while ciudad_candidato_str == False:
        ciudad_candidato_str = input("Introduce la ciudad: ")
        ciudad_candidato_str = fn_limpiar_ciudad(ciudad_candidato_str)

    #AÑADIR DATOS DEL CANDIDATO A UN DICCIONARIO
    candidato_dict = {
        "dni": dni_candidato_str,
        "nombre": nombre_candidato_str,
        "apellidos": apellidos_candidato_str,
        "edad": edad_candidato_int,
        "ciudad": ciudad_candidato_str
    }

    print(candidato_dict)        
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