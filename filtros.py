#IMPORTAR LA LISTA DE CANDIDATOS DE ALMACENAMIENTO - JARA
from almacenamiento import candidatos_lst

#IMPORTACIÓN DE VALIDACIONES - JARA
from validaciones import fn_validar_estudios

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