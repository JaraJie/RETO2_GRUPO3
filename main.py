#IMPORTACIÓN DE OS Y JSON - JARA
import os
import json

#LISTA DE CANDIDATOS - JARA
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

'''#FUNCIÓN PARA CARGAR LOS CANDIDATOS DE JSON - JARA
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
            candidatos_lst = json.loads(contenido_str)'''

#Función para validar DNI - JARA
def fn_validar_dni(dni_validar_str):

    """
    Valida el formato del DNI y comprueba que no esté registrado

    Elimina espacios exteriores y hace que la letra este
    en mayúsculas

    Argumentos:
        dni_validar_str (str): DNI introducido por el usuario

    Returns:
        str: devuelve el DNI corregido
    """

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

    #Comprobar que el DNI no este registrado anteriormente
    for candidato_str in candidatos_lst:
        if candidato_str["dni"] == dni_validar_str:
            print("Este DNI ya está registrado. Introduce otro.")
            return False
    
    return dni_validar_str

#Función limpiar y validar nombre - JARA
def fn_limpiar_nombre(nombre_validar_str):

    """
    Limpia y valida el nombre del candidato

    Elimina espacios exteriores, hace que la primera letra
    de cada palabra sea mayúscula y permite nombres compuestos
    separados por espacios

    Argumentos:
        nombre_validar_str (str): Nombre introducido

    Returns:
        str: devuelve el nombre corregido
    """
    
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

#Función limpiar y validar apellidos - JARA
def fn_limpiar_apellidos(apellidos_validar_str):

    """
    Limpia y valida los apellidos del candidato

    Elimina espacios exteriores, hace que la primera letra
    de cada palabra sea mayúscula y permite apellidos compuestos

    Argumentos:
        apellidos_validar_str (str): Apellidos introducidos

    Returns:
        str: devuelve los apellidos corregido
    """

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

#Función para validar edad - JARA
def fn_validar_edad (edad_validar_str):

    """
    Valida la edad del candidato y comprueba que sea igual
    o superior a 18 años

    Argumentos:
        edad_validar_str (str): Edad introducida por el usuario

    Returns:
        int: devuelve la edad convertida en integer
    """

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

#Función para limpiar y validar ciudad - JARA
def fn_limpiar_ciudad(ciudad_validar_str):

    """
    Limpia y valida la ciudad de residencia del candidato

    Elimina espacios exteriores, hace que la primera letra
    de cada palabra sea mayúscula y permite guiones

    Argumentos:
        ciudad_validar_str (str): Ciudad introducida

    Returns:
        str: devuelve la ciudad corregida
    """
    
    #Elimina espacios (inicio/final) y convierte todo en minúsculas menos la primera letra de cada palabra
    ciudad_validar_str = ciudad_validar_str.strip().title()

    #Comprobar que no deja el espacio en blanco
    if ciudad_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    #Comprobar que la ciudad contienen letras, permitiendo espacios y guiones
    if not ciudad_validar_str.replace(" ","").replace("-","").isalpha():
        print("La ciudad solo puede contener letras.")
        return False

    return ciudad_validar_str

#Función para limpiar y validar email - JARA
def fn_validar_email(email_validar_str):
    
    """
    Valida el correo electrónico del candidato

    Comprueba si contiene un único @, no contiene espacios
    y termina con .es o .com

    Argumentos:
        email_validar_str (str): Correo electrónico introducido

    Returns:
        str: devuelve el email
    """

    #Elimina espacios (inicio/final) y convierte todo en minúsculas
    email_validar_str = email_validar_str.strip().lower()

    #Comprobar que no deja el espacio en blanco
    if email_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    #Comprobar que contiene solo 1 @
    if email_validar_str.count("@") != 1:
        print("El email debe contener una única @.")
        return False

    #Comprobar que no tiene espacios (dentro del email)
    if " " in email_validar_str:
        print("El email no puede contener espacios.")
        return False

    #Comprobar que el email termina con .es o .com
    if not email_validar_str.endswith(".es") and not email_validar_str.endswith(".com"):
        print("El email debe terminar con '.es' o '.com'")
        return False

    #Comprobar que el email no empieza con @
    if email_validar_str.startswith("@"):
        print("El email debe contener un usuario antes de la @.")
        return False

    #Comprobar que el emial no termina con @.es ni @.com
    if email_validar_str.endswith("@.es") or email_validar_str.endswith("@.com"):
        print("El email debe contener un dominio.")
        return False

    return email_validar_str

#Función para validar teléfono - JARA
def fn_validar_telefono(telefono_validar_str):
     
    """
    Valida el número de teléfono del candidato

    Comprueba que contenga exactamente 9 caracteres númericos

    Argumentos:
        telefono_validar_str (str): Teléfono introducid

    Returns:
        str: devuelve el telefono
    """

    #Elimina espacios (inicio/final)
    telefono_validar_str = telefono_validar_str.strip()

    #Comprobar que no deja el espacio en blanco
    if telefono_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    #Comprobar que el telefono tiene 9 caracteres
    if len(telefono_validar_str) != 9:
        print("El teléfono debe contener 9 dígitos.")
        return False

    #Comprobar si son números
    if not telefono_validar_str.isdigit():
        print("El teléfono solo puede contener números.")
        return False

    return telefono_validar_str

#Función para seleccionar nivel de estudios - JARA
def fn_validar_estudios():
     
    """
    Solicita y valida el nivel de estudios del candidato

    Muestra las opciones disponibles y repite la solicitud
    hasta que el usuario seleccione una opción válida

    Returns:
        str: devuelve el nivel de estudios seleccionado
    """

    #Muestra las opciones disponibles
    print("""
              NIVEL DE ESTUDIOS
        --------------------------------
        1. Sin estudios
        2. ESO
        3. Bachillerato
        4. FP Medio
        5. FP Superior
        6. Grado universitario
        7. Máster
        8. Doctorado
        --------------------------------
        """)

    #En caso de que el usuario no intruduzca una opción valida continuará dentro del bucle
    while True:

        #Solicitar opción al candidato
        estudios_validar_str = input("\nSelecciona tu nivel de estudios (1-8): ")

        #Dependiendo de lo que se escoja guardara diferentes niveles
        if estudios_validar_str == "1":
            estudios_validar_str = "Sin estudios"

        elif estudios_validar_str == "2":
            estudios_validar_str = "ESO"

        elif estudios_validar_str == "3":
            estudios_validar_str = "Bachillerato"

        elif estudios_validar_str == "4":
            estudios_validar_str = "FP Medio"

        elif estudios_validar_str == "5":
            estudios_validar_str = "FP Superior"

        elif estudios_validar_str == "6":
            estudios_validar_str = "Grado universitario"

        elif estudios_validar_str == "7":
            estudios_validar_str = "Master"

        elif estudios_validar_str == "8":
            estudios_validar_str = "Doctorado"

        #En caso de que no escoja una opción valida continuará dentro del bucle
        else:
            print("Opción no válida. Introduce un número del 1 al 8.")
            continue

        return estudios_validar_str

#Función para validar titulación - JARA
def fn_validar_titulacion(titulacion_validar_str):

    """
    Limpia y valida la titulación académica del candidato.

    Elimina espacios exteriores y hace que la primera letra
    de cada palabra sea mayúscula.

    Argumentos:
        titulacion_validar_str (str): Titulación introducida

    Returns:
        str: devuelve la titulación corregida
    """

    #Elimina espacios (inicio/final) y convierte todo en minúsculas menos la primera letra de cada palabra
    titulacion_validar_str = titulacion_validar_str.strip().title()

    #Comprobar que no deja el espacio en blanco
    if titulacion_validar_str == "":
            print("Tienes que rellenar este campo.")
            return False

    return titulacion_validar_str
    
#Función para validar experiencia - JARA
def fn_validar_experiencia(experiencia_validar_str):

    """
    Valida los años de experiencia laboral del candidato

    Comprueba que el valor sea un número entero igual o
    superior a cero

    Argumentos:
        experiencia_validar_str (str): Años de experiencia

    Returns:
        int: devuelve la experiencia convertida en integer
    """

    #Elimina espacios (inicio/final)
    experiencia_validar_str = experiencia_validar_str.strip()

    #Comprobar que no deja el espacio en blanco
    if experiencia_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    #Comprobar que introduce un número entero y positivo
    if not experiencia_validar_str.isdigit():
        print("La experiencia debe ser un número entero igual o superior a 0.")
        return False

    #Convertir la experiencia de texto a número
    experiencia_validar_int = int(experiencia_validar_str)

    return experiencia_validar_int

#Función para validar puesto solicitado - JARA
def fn_validar_puesto(puesto_validar_str):

    """
    Limpia y valida el puesto solicitado por el candidato

    Elimina espacios exteriores y hace que la primera letra
    de cada palabra sea mayúscula

    Argumentos:
        puesto_validar_str (str): Puesto solicitado

    Returns:
        str: devuelve el puesto corregido
    """

    #Elimina espacios (inicio/final) y convierte todo en minúsculas menos la primera letra de cada palabra
    puesto_validar_str = puesto_validar_str.strip().title()

    #Comprobar que no deja el espacio en blanco
    if puesto_validar_str == "":
        print("Tienes que rellenar este campo.")
        return False

    return puesto_validar_str

#Función para introducir competencias técnicas - JARA
def fn_introducir_competencias():

    """
    Solicita las competencias técnicas del candidato

    Permite introducir varias competencias, evita duplicados
    y finaliza cuando el usuario escribe FIN

    Returns:
        lst: devuelve una lista de competencias técnicas introducidas
    """

    #Crear una lista para las competencias
    competencias_lst = []

    #Mostrar instrucciones
    print("\nIntroduce las competencias técnicas.")
    print("Al finalizar escriba 'FIN'.")

    #Bucle infinito hasta que el usuario escriba fin
    while True:

        #solicitar competencias al candidato
        competencia_str = input("\nCompentencia técnica: ")

        #Elimina espacios (inicio/final) y convierte todo en minúsculas menos la primera letra de cada palabra
        competencia_str = competencia_str.strip().title()

        #Comprobar que no deja el espacio en blanco
        if competencia_str == "":
            print("Tienes que rellenar este campo.")
            continue

        #En caso de que el usuario escriba fin y no hay competencias en la lista que le pida que escriba al menos una
        if competencia_str == "Fin":
            if len(competencias_lst) == 0:
                print("Debes introducir al menos una competencia técnica.")
                continue
            break #Finalizar el bucle

        #Comprobar si la competencia estaba en la lista
        if competencia_str in competencias_lst:
            print("Esa competencia ya está introducida.")
            continue

        #Añadir competencias escritas por el candidato a la lista
        competencias_lst.append(competencia_str)

    return competencias_lst

#Función para introducir idiomas - JARA
def fn_introducir_idiomas():

    """
    Solicita los idiomas del candidato

    Permite introducir varios idiomas, evita duplicados
    y finaliza cuando el usuario escribe FIN

    Returns:
        lst: devuelve una lista de idiomas introducidas
    """

    #Crear una lista para los idiomas
    idiomas_lst = []

    #Mostrar instrucciones
    print("\nIntroduce los idiomas.")
    print("Al finalizar escriba 'FIN'.")

    #Bucle infinito hasta que el usuario escriba fin
    while True:

        #solicitar idiomas al candidato
        idioma_str = input("\nIdioma: ")

        #Elimina espacios (inicio/final) y convierte todo en minúsculas menos la primera letra de cada palabra
        idioma_str = idioma_str.strip().title()

        #Comprobar que no deja el espacio en blanco
        if idioma_str == "":
            print("Tienes que rellenar este campo.")
            continue

        #En caso de que el usuario escriba fin y no hay idiomas en la lista que le pida que escriba al menos una
        if idioma_str == "Fin":
            if len(idiomas_lst) == 0:
                print("Debes introducir al menos un idioma.")
                continue
            break #Finalizar el bucle

        #Comprobar si el idioma estaba en la lista
        if idioma_str in idiomas_lst:
            print("Ese idioma ya está introducido.")
            continue

        #Añadir idiomas introducidas por el candidato a la lista
        idiomas_lst.append(idioma_str)

    return idiomas_lst

#Función para filtrar candidato por experiencia - JARA
def fn_filtrar_experiencia():

    """
    Filtra los candidatos según los años mínimos de experiencia

    Solicita los años de experiencia al usuario, comprueba
    que sean válidos y muestra los candidatos que cumplen
    con el mínimo solicitado
    """

    print("\n--- FILTRAR POR EXPERIENCIA ---")

    #Bucle infinito hasta que el usuario introduzca un número valido
    while True:

        #Solicita años de experiencia
        experiencia_introducida_str = input("\nIntroduzca los años de experiencia mínimos: ")

        #Borrar espacios (inicio/final)
        experiencia_introducida_str = experiencia_introducida_str.strip()

        #Comprobar que el campo no este vaco
        if experiencia_introducida_str == "":
            print("Tienes que rellenar este campo.")

        #Comprobar si la experiencia es un dígito numérico
        elif not experiencia_introducida_str.isdigit():
            print("La experiencia debe ser un número entero igual o superior a 0.")

        else:

            #Convierte la esperiencia de texto a número
            experiencia_introducida_int = int(experiencia_introducida_str)

            #Crear lista para candidatos filtrados
            candidatos_filtrados_lst = []

            #Recorrer candidatos dentro de la lista
            for candidato_dict in candidatos_lst:

                #Comprueba que la experiencia dentro de los candidatos disponibles sea superior o igual a la introducida por el usuario
                if candidato_dict["experiencia"] >= experiencia_introducida_int:

                    #Añade esos candidatos a la lista
                    candidatos_filtrados_lst.append(candidato_dict)

            #En caso de que la lista este vacía y no haya candidatos
            if len(candidatos_filtrados_lst) == 0:
                print("No hay candidatos disponibles con esa experiencia.")

            else:

                #Muestra los candidatos disponibles con esa experiencia
                print()
                print("CANDIDATOS DISPONIBLES CON", experiencia_introducida_int, "AÑOS DE EXPERIENCIA")
                print("------------------------------------------")

                for candidato_dict in candidatos_filtrados_lst:

                    for clave, valor in candidato_dict.items():

                        print(" -", clave, ":", valor)
                    print("-------------------------------")
            break #Sale del bucle

#Función para filtrar candidatos por estudios - JARA
def fn_filtrar_estudios():

    """
    Filtra los candidatos según su nivel de estudios

    Solicita un nivel de estudios y muestra los candidatos
    que tienen ese mismo nivel o uno superior
    """

    print("\n---FILTRAR POR ESTUDIOS---")

    #Solicitar y validar el nivel de estudios
    estudios_introducidos_str = fn_validar_estudios()

    #Crear lista para candidatos filtrados
    candidatos_filtrados_lst = []

    #Lista de niveles de estudios y su valor correspondiente (bachillerato y fp medio se consideran el mismo nivel)
    estudios_dict = {
        "Sin estudios": 0,
        "ESO": 1,
        "Bachillerato": 2,
        "FP Medio": 2,
        "FP Superior": 3,
        "Grado universitario": 4,
        "Master": 5,
        "Doctorado": 6
    }

    #Obtiene el valor correspondiente al nivel de estudios seleccionado
    posicion_estudios_introducidos_int = estudios_dict[estudios_introducidos_str]

    #Recorrer candidatos dentro de la lista
    for candidato_dict in candidatos_lst:

        #Obtiene el valor correspondiente a los estudios del candidato
        posicion_estudios_candidato_int = estudios_dict[candidato_dict["estudios"]]

        #Comprueba si los estudios del candidato son iguales o superiores
        if posicion_estudios_candidato_int >= posicion_estudios_introducidos_int:

            #Añade los candidatos a la lista
            candidatos_filtrados_lst.append(candidato_dict)

    #Comprueba si hay candidatos disponibles
    if len(candidatos_filtrados_lst) == 0:
        print("No hay candidatos disponibles con esos estudios o superiores.")

    else:

        #Mostrar los candidatos disponibles con estudios igual o superiores al seleccionado
        print()
        print("CANDIDATOS CON ESTUDIOS IGUALES O SUPERIORES A:", estudios_introducidos_str)
        print("------------------------------------------")

        for candidato_dict in candidatos_filtrados_lst:

            for clave, valor in candidato_dict.items():

                print(" -", clave, ":", valor)
            print("-------------------------------")

#Función para filtrar candidato por competencias - JARA
def fn_filtrar_competencias():

    """
    Filtra los candidatos según sus competencias técnicas

    Muestra las competencias disponibles, solicita una
    competencia al usuario y muestra los candidatos
    que tengan esa competencia
    """

    print("\n--- FILTRAR POR COMPETENCIAS TÉCNICAS ---")

    #Crear lista para almacenar las competencias guardadas en json
    competencias_disponibles_lst = []

    #Recorrer candidatos disponibles dentro de la lista de candidatos
    for candidato_dict in candidatos_lst:

        #Recorrer las competencias de cada candidato
        for competencia_str in candidato_dict["competencias_tecnicas"]:

            #Añadir las competencias técnicas de cada candidato a una lista
            competencias_disponibles_lst.append(competencia_str)

    #Convertr lista en set para evitar repeticiones
    competencias_disponibles_set = set(competencias_disponibles_lst)

    #Mostrar las competencias técnicas disponibles de los candidatos
    print("\nCOMPETENCIAS TÉCNICAS DISPONIBLES:")
    print("------------------------------------------")
    for competencia_str in competencias_disponibles_set:

        print(" -", competencia_str)

    #Bucle infinito hasta que el usuario escriba una competencia correcta
    while True:

        #Solicitar la competencia técnica al usuario
        competencia_introducida_str = input("\nIntroduzca la competencia técnica que desea buscar: ")

        #Borrar espacios (inicio/fin) y convertir la primera letra en mayúsculas y el resto en minúsculas
        competencia_introducida_str = competencia_introducida_str.strip().title()

        #Comprobar que el campo no está vacío
        if competencia_introducida_str == "":
            print("Tienes que introducir una competencia técnica.")

        else:

            #Comrpobar si la competencia introducida existe entre las competencias disponibles
            if competencia_introducida_str not in competencias_disponibles_set:
                print("No hay candidatos disponibles con esa competencia técnica.")

            else:

                #Crear lista de candidatos filtrados con la competencia pedida
                candidatos_filtrados_lst = []

                #Recorrer candidatos dentro de la lista
                for candidato_dict in candidatos_lst:

                    #Comprobar si el candidato tiene la competencia pedida
                    if competencia_introducida_str in candidato_dict["competencias_tecnicas"]:

                        #Añadir candidato a la lista de candidatos disponibles con esa cometencia
                        candidatos_filtrados_lst.append(candidato_dict)

                #Mostrar los candidatos disponibles con esa competencia técnica
                print()
                print("CANDIDATOS DISPONIBLES CON LA COMPETENCIA:", competencia_introducida_str)
                print("------------------------------------------")

                for candidato_dict in candidatos_filtrados_lst:

                    for clave, valor in candidato_dict.items():

                        print(" -", clave, ":", valor)
                    print("-------------------------------")
            
            break #Sale del bucle

# OPCIÓN 1. REGISTRAR NUEVO CANDIDATO - JARA
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

#OPCIÓN 2. MODIFICAR CANDIDATO - JARA
def fn_modificar_candidato():

    """
    Permite modificar los datos personales y profesionales
    de un candidato ya registrado

    Muestra los candidatos disponibles (su DNI), permite seleccionar
    qué datos modificar y comprueba si la nueva información es correcta

    Guarda los cambios realizados en el archivo.json
    """

    os.system('cls')

    #Comprobar si existen candidatos
    if len(candidatos_lst) == 0:
        print("Aún no hay candidatos disponibles.")

    #En caso de que existan muestra lo siguiente.
    else:

        #Muestra los DNI de los candidatos disponibles
        print("\n--- CANDIDATOS DISPONIBLES ---\n")

        for candidato_dict in candidatos_lst:
            print(" -", candidato_dict["dni"])

        #Solitar DNI del candidato que desea modificar
        dni_str = input("\nIntroduce el DNI del candidato que deseas modificar: ")

        #Eliminar espacios (inicio/final) y convertir la letra en mayúscula
        dni_str = dni_str.strip().upper()

        #Crear una variable para comprobar si el candidato existe
        candidato_encontrado_bool = False

        #Recorre la lista de candidatos para buscar si el DNI introducido coincide
        for candidato_dict in candidatos_lst:

            if candidato_dict["dni"] == dni_str:

                #En caso de que el DNI coincida el valor se volvera cierto
                candidato_encontrado_bool = True

                #Bucle infinito para permitir modificar varios datos hasta que se pulse salir
                while True:
                    
                    #Muestra los datos del candidato
                    print("""
                    -------------------------------
                        MODIFICAR CANDIDATO
                    -------------------------------
                    """)

                    print("Datos disponibles:\n")
                    print("1. Nombre:", candidato_dict["nombre"])
                    print("2. Apellidos:", candidato_dict["apellidos"])
                    print("3. Edad:", candidato_dict["edad"])
                    print("4. Ciudad:", candidato_dict["ciudad"])
                    print("5. Email:", candidato_dict["email"])
                    print("6. Teléfono:", candidato_dict["telefono"])
                    print("7. Estudios:", candidato_dict["estudios"])
                    print("8. Titulación:", candidato_dict["titulacion"])
                    print("9. Experiencia:", candidato_dict["experiencia"])
                    print("10. Puesto solicitado:", candidato_dict["puesto_solicitado"])
                    print("11. Competencias técnicas:", candidato_dict["competencias_tecnicas"])
                    print("12. Idiomas:", candidato_dict["idiomas"])
                    print("0. Guardar y salir")


                    #Solicita que dato desea modificar
                    dato_modificar_str = input("\n¿Qué dato deseas modificar? ")
                    
                    #Eliminar espacios (inicio/final)
                    dato_modificar_str = dato_modificar_str.strip()

                    #MODIFICAR NOMBRE
                    if dato_modificar_str == "1":
                        nombre_nuevo_str = input("Nuevo nombre: ")
                        nombre_nuevo_str = fn_limpiar_nombre(nombre_nuevo_str)

                        while nombre_nuevo_str == False:
                            nombre_nuevo_str = input("Nuevo nombre: ")
                            nombre_nuevo_str = fn_limpiar_nombre(nombre_nuevo_str)

                        candidato_dict["nombre"] = nombre_nuevo_str

                    #MODIFICAR APELLIDOS
                    elif dato_modificar_str == "2":
                        apellidos_nuevos_str = input("Nuevos apellidos: ")
                        apellidos_nuevos_str = fn_limpiar_apellidos(apellidos_nuevos_str)

                        while apellidos_nuevos_str == False:
                            apellidos_nuevos_str = input("Nuevos apellidos: ")
                            apellidos_nuevos_str = fn_limpiar_apellidos(apellidos_nuevos_str)

                        candidato_dict["apellidos"] = apellidos_nuevos_str

                    #MODIFICAR EDAD
                    elif dato_modificar_str == "3":
                        edad_nueva_int = input("Nueva edad: ")
                        edad_nueva_int = fn_validar_edad(edad_nueva_int)

                        while edad_nueva_int == False:
                            edad_nueva_int = input("Nueva edad: ")
                            edad_nueva_int = fn_validar_edad(edad_nueva_int)

                        candidato_dict["edad"] = edad_nueva_int

                    #MODIFICAR CIUDAD
                    elif dato_modificar_str == "4":
                        ciudad_nueva_str = input("Nueva ciudad: ")
                        ciudad_nueva_str = fn_limpiar_ciudad(ciudad_nueva_str)

                        while ciudad_nueva_str == False:
                            ciudad_nueva_str = input("Nueva ciudad: ")
                            ciudad_nueva_str = fn_limpiar_ciudad(ciudad_nueva_str)

                        candidato_dict["ciudad"] = ciudad_nueva_str

                    #MODIFICAR EMIAL
                    elif dato_modificar_str == "5":
                        email_nuevo_str = input("Nuevo email: ")
                        email_nuevo_str = fn_validar_email(email_nuevo_str)

                        while email_nuevo_str == False:
                            email_nuevo_str = input("Nuevo email: ")
                            email_nuevo_str = fn_validar_email(email_nuevo_str)

                        candidato_dict["email"] = email_nuevo_str

                    #MODIFICAR TELÉFONO
                    elif dato_modificar_str == "6":
                        telefono_nuevo_str = input("Nuevo teléfono: ")
                        telefono_nuevo_str = fn_validar_telefono(telefono_nuevo_str)

                        while telefono_nuevo_str == False:
                            telefono_nuevo_str = input("Nuevo teléfono: ")
                            telefono_nuevo_str = fn_validar_telefono(telefono_nuevo_str)

                        candidato_dict["telefono"] = telefono_nuevo_str

                    #MODIFICAR ESTUDIOS
                    elif dato_modificar_str == "7":
                        candidato_dict["estudios"] = fn_validar_estudios()

                    #MODIFICAR TITULACIÓN
                    elif dato_modificar_str == "8":
                        titulacion_nueva_str = input("Nueva titulación: ")
                        titulacion_nueva_str = fn_validar_titulacion(titulacion_nueva_str)

                        while titulacion_nueva_str == False:
                            titulacion_nueva_str = input("Nueva titulación: ")
                            titulacion_nueva_str = fn_validar_titulacion(titulacion_nueva_str)

                        candidato_dict["titulacion"] = titulacion_nueva_str
                    
                    #MODIFICAR EXPERIENCIA
                    elif dato_modificar_str == "9":
                        experiencia_nueva_int = input("Nuevos años de experiencia: ")
                        experiencia_nueva_int = fn_validar_experiencia(experiencia_nueva_int)

                        while experiencia_nueva_int is False:
                            experiencia_nueva_int = input("Nuevos años de experiencia: ")
                            experiencia_nueva_int = fn_validar_experiencia(experiencia_nueva_int)

                        candidato_dict["experiencia"] = experiencia_nueva_int

                    #MODIFICAR PUESTO
                    elif dato_modificar_str == "10":
                        puesto_nuevo_str = input("Nuevo puesto solicitado: ")
                        puesto_nuevo_str = fn_validar_puesto(puesto_nuevo_str)

                        while puesto_nuevo_str == False:
                            puesto_nuevo_str = input("Nuevo puesto solicitado: ")
                            puesto_nuevo_str = fn_validar_puesto(puesto_nuevo_str)

                        candidato_dict["puesto_solicitado"] = puesto_nuevo_str

                    #MOFICAR COMPETENCIAS TÉCNICAS
                    elif dato_modificar_str == "11":

                        #Mostrar mensaje de que se eliminaran y sobreescribiran las competencias
                        print("\nAVISO: Se eliminarán todas las competencias anteriores.")
                        candidato_dict["competencias_tecnicas"] = fn_introducir_competencias()

                    #MODIFICAR IDIOMAS
                    elif dato_modificar_str == "12":

                        #Mostrar mensaje de que se eliminaran y sobreescribiran los idiomas
                        print("\nAVISO: Se eliminarán todos los idiomas anteriores.")
                        candidato_dict["idiomas"] = fn_introducir_idiomas()

                    #Salir del bucle y guardar datos en archivo.json
                    elif dato_modificar_str == "0":
                        fn_guardar_candidatos()
                        break

                    #En caso de que pulse una opción no disponible
                    else:
                        print("Opción no válida.")

        #Si el candidato no se ha encontrado
        if candidato_encontrado_bool == False:
            print("\nNo se ha encontrado ningún candidato con ese DNI.")
            print("Comprueba que has introducido correctamente el DNI (8 números y 1 letra).")

#OPCIÓN 3. MOSTRAR TODOS LOS CANDIDATOS - JARA
def fn_mostrar_candidatos():

    """
    Muestra la información de todos los candidatos registrados

    Comprueba si existen candidatos en la lista y
    recorre la lista mostrando los datos de cada candidato
    """

    os.system('cls')

    #Comprobar si la lista de candidatos esta vacía
    if len(candidatos_lst) == 0:
            print("Aún no hay candidatos disponibles.")

    #Si hay candidatos registrados muestra su información
    else:
        print("""
        -------------------------------
            LISTA DE CANDIDATOS
        -------------------------------""")

        #Inicializar el contador para numerar los candidatos
        candidato_int = 0

        #Recorrer todos los candidatos almacenados en la lista
        for candidato_dict in candidatos_lst:

            #Sumar uno al contador por cada candidato
            candidato_int += 1

            #Mostrar número de candidato, va por orden de registro
            print("\nCANDIDATO Nº", candidato_int)
            print("-------------------------------")

            #Recorrer el diccionario del candidato para mostrar sus datos
            for clave, valor in candidato_dict.items():
                print(" -", clave," :", valor)
            print("-------------------------------")

        print("\n--- FIN DE LA LISTA DE CANDIDATOS ---")

#OPCIÓN 4. BUSCAR CANDIDATO
def fn_buscar_candidato():
    print("W.I.P.")

#OPCIÓN 5. FILTRAR CANDIDATOS - JARA
def fn_filtrar_candidatos():

    os.system('cls')

    #Comprobar si hay candidatos registrados en el archivo.json
    if len(candidatos_lst) == 0:
        print("Aún no hay candidatos disponibles.")

    else:

        #Bucle infinito para que el usuario seleccione una opción valida
        while True:
            print("""
            -------------------------------
                LISTA DE CANDIDATOS
            -------------------------------
            
            1. Filtrar por experiencia
            2. Filtrar por estudios
            3. Filtrar por competencias técnicas
            0. Salir
            """)

            #Solicita que filtro quiere usar
            filtro_seleccionado_str = input("¿Qué tipo de filtro deseas utilizar?: ")
            
            #Elimina espacios(inicio/final)
            filtro_seleccionado_str = filtro_seleccionado_str.strip()

            #Funcion por experiencia
            if filtro_seleccionado_str == "1":
                fn_filtrar_experiencia()

            #Filtrar por nivel estudios
            elif filtro_seleccionado_str == "2":
                fn_filtrar_estudios()

            #Filtrar por competencias técnicas
            elif filtro_seleccionado_str == "3":
                fn_filtrar_competencias()

            #Salir del bucle
            elif filtro_seleccionado_str == "0":
                break

            #Volver a preguntar input
            else:
                print("Opción no disponible.")

#OPCIÓN 6. ELIMINAR CANDIDATOS
def fn_eliminar_candidato():
    print("W.I.P.")

#OPCIÓN 7. GESTIONAR CANDIDATURAS
def fn_gestionar_candidaturas():
    print("W.I.P.")

#OPCIÓN 8. EXPORTAR INFORMES - JARA
def fn_exportar_informes():
    print("W.I.P.")

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

'''#Ejecuta la función con los cantitados guardados - JARA
fn_cargar_candidatos()'''

#Abrir y leer el archivo.json - JARA
with open("candidatos.json", "r") as x:

    #Todo lo que lea en el archivo.json estará en la siguiente variable
    contenido_str = x.read()

    #En caso de que el contenido este vacio creará una lista
    if contenido_str == "":
        candidatos_lst = []
    
    #Si no abrira el archivo y su contenido
    else:
        candidatos_lst = json.loads(contenido_str)

#Ejecuta el programa - JARA
fn_menu()