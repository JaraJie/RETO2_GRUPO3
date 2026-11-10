#IMPORTAR OS - JARA
import os

#IMPORTACIÓN DE ALMACENAMIENTO - JARA
from almacenamiento import candidatos_lst, fn_guardar_candidatos

#IMPORTACIÓN DE VALIDACIONES - JARA
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
#IMPORTACIÓN DE FILTROS
from filtros import (
    fn_filtrar_experiencia,
    fn_filtrar_estudios,
    fn_filtrar_competencias
)

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

#OPCIÓN 4. BUSCAR CANDIDATO - ASIER
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

#OPCIÓN 6. ELIMINAR CANDIDATOS - MIKEL
def fn_eliminar_candidato():

    os.system('cls')

    #Comprobar si la lista de candidatos está vacía
    if len(candidatos_lst) == 0:
        print("Aún no hay candidatos disponibles.")

    else:

        print("""
        -------------------------------
             ELIMINAR CANDIDATO
        -------------------------------""")

        # contador de candidatos
        candidato_int = 0

         # recorremos los candidatos dentro de la lista de candidatos
        for candidato_dict in candidatos_lst:

            # sumamos 1 al contador del candidato
            candidato_int += 1

            print("\nCANDIDATO Nº", candidato_int)

            # mostramos los datos de los candidatos disponibles(nombres, apellidos y dni)
            print("Nombre:", candidato_dict["nombre"], candidato_dict["apellidos"])
            print("DNI:", candidato_dict["dni"])

        # solicitamos el input al usuario
        dni_str = input("\nIntroduce el DNI del candidato que quieres eliminar: ")

        # hacemos una variable con el valor de false 
        candidato_encontrado_bool = False
        
        # recorremos los candidatos dentro de la lista de candidatos 
        for candidato_dict in candidatos_lst:

            # comprobamos que el dni introducido lo tenga un candidato
            if candidato_dict["dni"] == dni_str:

                # si encontramos el candidato  la variable se volvera true
                candidato_encontrado_bool = True

                # solicitamos input de nuevo 
                confirmar_str = input("\n¿Estás seguro de que quieres eliminar este candidato? (si/no): ").lower()

                # si la respuesta es afirmativo elimina el candidato de la lista
                if confirmar_str == "si":

                    candidatos_lst.remove(candidato_dict)

                    print("\n--- CANDIDATO ELIMINADO CORRECTAMENTE ---")

                    # guardamos los datos 
                    fn_guardar_candidatos()

                # si no la eliminacion se cancela (escribiendo no o cualquier otra cosa)
                else:
                    print("Eliminación cancelada.")

        # en caso de que no haya candidatos con ese dni
        if candidato_encontrado_bool == False:
            print("No se ha encontrado ningún candidato con ese DNI.")

#OPCIÓN 7. GESTIONAR CANDIDATURAS - XABIER
def fn_gestionar_candidaturas():
    print("W.I.P.")

#OPCIÓN 8. EXPORTAR INFORMES - JARA
def fn_exportar_informes():

    """
    Exporta informes con la información de los candidatos

    Permite generar informes a partir de los datos
    almacenados en el archivo.json
    """

    os.system('cls')

    #Comprobar si existen candidatos registrados
    if len(candidatos_lst) == 0:
        print("Aún no hay candidatos disponibles para exportar.")

    else:

        #Abre el archivo informes.txt en modo escritura
        with open("informes.txt", "w") as x:

            #Escribe el sigueiente texto
            x.write("------------------------------------------\n")
            x.write("        INFORME DE CANDIDATOS\n")
            x.write("              TALENTCONNECT\n")
            x.write("------------------------------------------\n")

            #Contador de candidatos
            candidato_int = 0

            #Recorre todos los candidatos dentro de la lista
            for candidato_dict in candidatos_lst:

                #Suma uno al contador de candidatos
                candidato_int += 1

                #Escribe el número de candidato
                x.write("\nCANDIDATO NUMERO " + str(candidato_int) + "\n")
                x.write("------------------------------------------\n")

                #Recorre los datos de cada candidato
                for clave, valor in candidato_dict.items():

                    #Escribe los datos por cada candidato
                    x.write(str(clave) + ": " + str(valor) + "\n")
                
            x.write("------------------------------------------\n")

        #Mostrar mensaje de que los informes se han exportado correctamente
        print("--- INFORMES EXPORTADOS CORRECTAMENTE ---")
        print("El archivo informes.txt se ha creado correctamente.")