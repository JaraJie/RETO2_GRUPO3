#IMPORTAR JSON - JARA
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

#FUNCIÓN PARA CARGAR LOS CANDIDATOS DE JSON - JARA
def fn_cargar_candidatos(cargar_candidatos_lst):

    """
    Cargar los candidatos almacenados en el archivo JSON

    Leer el contenido de candidatos.json y cargar los datos
    para usarlos durante la ejecución del programa

    Argumentos:
        cargar_candidatos_lst: lista donde se almacenarán los candidatos de json

    Return:
        lst: devuelve la lista de candidatos cargada desde json
    """

    #Abrir y leer el archivo.json
    with open("candidatos.json", "r") as x:

        #Todo lo que lea en el archivo.json estará en la siguiente variable
        contenido_str = x.read()

        #En caso de que el contenido este vacio creará una lista
        if contenido_str == "":
            cargar_candidatos_lst = []
        
        #Si no abrira el archivo y su contenido
        else:
            cargar_candidatos_lst = json.loads(contenido_str)

        return cargar_candidatos_lst