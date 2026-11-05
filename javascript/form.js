//AUTOR: JARA
//JAVASCRIPT PARA FORM_CV.HTML

//FUNCIÓN PARA VALIDAR FORMULARIO
function validarFormulario(event) {

    //EVITAMOS QUE LA PÁGINA SE RECARGUE
    //JARA: LOS BUSQUE EN INTERNET PORQUE NO PODIA COMPROBAR LOS DATOS EN LA CONSOLA Y ME DECIA DE PONER ESTO
    event.preventDefault();

    //RECOGEMOS LOS DATOS DEL USUARIO
    const nombre = document.getElementById("nombre").value.trim();
    const apellidos = document.getElementById("apellidos").value.trim();

    //MOSTRAMOS LOS DATOS EN LA CONSOLA
    console.log("Nombre:", nombre);
    console.log("Apellidos:", apellidos);

    //ALERTAMOS CON UN MENSAJE DE CONFIRMACIÓN
    alert("¡Perfecto! Tus datos se han validado correctamente.");

}

//RECORDAD Y PONER LOS DEMÁS DATOS PARA QUE SE GUARDE EN CONSOLA
//CREAR FUNCIONES PARA QUE LOS CAMPOS NO ESTEN VACIOS Y QUE ALERTE
//OTRAS FUNCIONES COMO LAS HEMOS HECHO EN CLASE DE QUE EL NOMBRE TENGA 3 CARÁCTERES POR LO MENOS