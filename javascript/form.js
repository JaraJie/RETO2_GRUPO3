//AUTOR: JARA
//JAVASCRIPT PARA FORM_CV.HTML

//FUNCIÓN PARA VALIDAR FORMULARIO
function validarFormulario(event) {

    //RECOGEMOS LOS DATOS DEL USUARIO
    const nombre = document.getElementById("nombre").value.trim();
    const apellidos = document.getElementById("apellidos").value.trim();

    //MOSTRAMOS LOS DATOS EN LA CONSOLA
    console.log("Nombre:", nombre);
    console.log("Apellidos:", apellidos);


    //ALERTAMOS CON UN MENSAJE DE CONFIRMACIÓN
    alert("¡Perfecto! Tus datos se han validado correctamente.");

}