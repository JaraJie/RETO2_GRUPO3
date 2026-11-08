#IMPORTAR OS
import os

#Importar de validaciones.py las siguientes funciones
from validaciones import (
    fn_validar_dni,
    fn_limpiar_nombre,
    fn_limpiar_apellidos,
    fn_validar_edad,
    fn_limpiar_ciudad,
    fn_validar_email,
    fn_validar_telefono,
    fn_validar_estudios,
    fn_validar_titulacion,
    fn_validar_experiencia,
    fn_validar_puesto,
    fn_introducir_competencias,
    fn_introducir_idiomas
)

# OPCIÓN 1. REGISTRAR NUEVO CANDIDATO
def fn_registrar_candidato():
    
    """
    Registra un nuevo candidato a TalentConnect

    Solicita los datos personales y profesionales,
    valida la información introducida y almacena
    al candidato en la lista y en el archivo JSON
    """

    os.system('cls')

    print("--- REGISTRO DE NUEVO CANDIDATO ---")

    #SOLICITAR DNI DEL CANDIDATO
    dni_candidato_str = input("\nIntroduce el DNI: ")

    #Llama a la función DNI y guarda el resultado en la variable
    dni_candidato_str = fn_validar_dni(dni_candidato_str)

    #Mientras que el DNI no sea valido, repetir la funcion de validación del DNI
    while dni_candidato_str == False:
        dni_candidato_str = input("\nIntroduce el DNI: ")
        dni_candidato_str = fn_validar_dni(dni_candidato_str)

    #SOLICITAR NOMBRE DEL CANDIDATO
    nombre_candidato_str = input("\nIntroduce el nombre: ")

    #Llama a la función nombre y guarda el resultado en la variable
    nombre_candidato_str = fn_limpiar_nombre(nombre_candidato_str)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while nombre_candidato_str == False:
        nombre_candidato_str = input("\nIntroduce el nombre: ")
        nombre_candidato_str = fn_limpiar_nombre(nombre_candidato_str)

    #SOLICITAR APELLIDOS DEL CANDIDATO
    apellidos_candidato_str = input("\nIntroduce los apellidos: ")

    #Llama a la función apellidos y guarda el resultado en la variable
    apellidos_candidato_str = fn_limpiar_apellidos(apellidos_candidato_str)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while apellidos_candidato_str == False:
        apellidos_candidato_str = input("\nIntroduce los apellidos: ")
        apellidos_candidato_str = fn_limpiar_apellidos(apellidos_candidato_str)

    #SOLICITAD EDAD DEL CANDIDATO
    edad_candidato_int = input("\nIntroduce la edad: ")

    #Llama a la función edad y guarda el resultado en la variable
    edad_candidato_int = fn_validar_edad(edad_candidato_int)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while edad_candidato_int == False:
        edad_candidato_int = input("\nIntroduce la edad: ")
        edad_candidato_int = fn_validar_edad(edad_candidato_int)

    #SOLICITAR CIUDAD DEL CANDIDATO
    ciudad_candidato_str = input("\nIntroduce la ciudad: ")

    #Llama a la función ciudad y guarda el resultado en la variable
    ciudad_candidato_str = fn_limpiar_ciudad(ciudad_candidato_str)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while ciudad_candidato_str == False:
        ciudad_candidato_str = input("\nIntroduce la ciudad: ")
        ciudad_candidato_str = fn_limpiar_ciudad(ciudad_candidato_str)

    #SOLICITAR EMAILL DEL CANDIDATO
    email_candidato_str = input("\nIntroduce el email: ")

    #Llama a la función email y guarda el resultado en la variable
    email_candidato_str = fn_validar_email(email_candidato_str)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while email_candidato_str == False:
        email_candidato_str = input("\nIntroduce el email: ")
        email_candidato_str = fn_validar_email(email_candidato_str)

    #SOLICITAR TELÉFONO DEL CANDIDATO
    telefono_candidato_str = input("\nIntroduce el teléfono: ")

    #Llama a la función telefono y guarda el resultado en la variable
    telefono_candidato_str = fn_validar_telefono(telefono_candidato_str)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while telefono_candidato_str == False:
        telefono_candidato_str = input("\nIntroduce el teléfono: ")
        telefono_candidato_str = fn_validar_telefono(telefono_candidato_str)

    #SOLICITAR NIVEL DE ESTUDIOS DEL CANDIDATO
    estudios_candidato_str = fn_validar_estudios()

    #SOLICITAR TITULACIÓN DEL CANDIDATO
    titulacion_candidato_str = input("\nIntroduce tu titulación: ")

    #Llama a la función titulación y guarda el resultado en la variable
    titulacion_candidato_str = fn_validar_titulacion(titulacion_candidato_str)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while titulacion_candidato_str == False:
        titulacion_candidato_str = input("\nIntroduce tu titulación: ")
        titulacion_candidato_str = fn_validar_titulacion(titulacion_candidato_str)

    #SOLICITAR EXPERIENCIA DEL CANDIDATO
    experiencia_candidato_int = input("\nIntroduce los años de experiencia: ")

    #Llama a la función experiencia y guarda el resultado en la variable
    experiencia_candidato_int = fn_validar_experiencia(experiencia_candidato_int)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while experiencia_candidato_int is False:
        experiencia_candidato_int = input("\nIntroduce los años de experiencia: ")
        experiencia_candidato_int = fn_validar_experiencia(experiencia_candidato_int)

    #SOLICITAR PUESTO DESEADO DEL CANDIDATO
    puesto_candidato_str = input("\nIntroduce el puesto solicitado: ")

    #Llama a la función candidato y guarda el resultado en la variable
    puesto_candidato_str = fn_validar_puesto(puesto_candidato_str)

    #Bucle infinito en caso de que la función te devuelva que es incorrecta
    while puesto_candidato_str == False:
        puesto_candidato_str = input("\nIntroduce el puesto solicitado: ")
        puesto_candidato_str = fn_validar_puesto(puesto_candidato_str)

    #SOLICITAR COMPETENCIAS DEL CANDIDATO
    competencias_candidato_lst = fn_introducir_competencias()

    #SOLICITAR IDIOMAS DEL CANDIDATO
    idiomas_candidato_lst = fn_introducir_idiomas()

    #AÑADIR DATOS DEL CANDIDATO A UN DICCIONARIO
    candidato_dict = {
        "dni": dni_candidato_str,
        "nombre": nombre_candidato_str,
        "apellidos": apellidos_candidato_str,
        "edad": edad_candidato_int,
        "ciudad": ciudad_candidato_str,
        "email": email_candidato_str,
        "telefono": telefono_candidato_str,
        "estudios": estudios_candidato_str,
        "titulacion": titulacion_candidato_str,
        "experiencia": experiencia_candidato_int,
        "puesto_solicitado": puesto_candidato_str,
        "competencias_tecnicas": competencias_candidato_lst,
        "idiomas": idiomas_candidato_lst,
        "estado": "En revision" #El estado inicial de la candidatura al crear un nuevo perfil siempre será "en revisión"
    }

    #Añadir diccionario del candidato a una lista
    candidatos_lst.append(candidato_dict)

    #Llamar a la función para que guarde el candidato registrado
    fn_guardar_candidatos()

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