//AUTOR: JARA, MIKEL, ASIER, XABIER
//JAVASCRIPT PARA FORM_CV.HTML

//FUNCIÓN PARA VALIDAR FORMULARIO
function validarFormulario(event) {

    //RECOGEMOS LOS DATOS DEL USUARIO
    const nombre = document.getElementById("nombre").value;
    const apellidos = document.getElementById("apellidos").value;
    const DNI = document.getElementById("DNI").value;
    const correo_electronico = document.getElementById("correo_electronico").value;
    const telefono = document.getElementById("telefono").value;

    //RECOGEMOS LOS DATOS DE FORMACIÓN ACADÉMICA
    const fecha_inicio_estudios = document.getElementById("fecha_inicio_estudios").value;
    const fecha_fin_estudios = document.getElementById("fecha_fin_estudios").value;

    //RECOGEMOS LOS DATOS DE EXPERIENCIA LABORAL
    const fecha_inicio_trabajo = document.getElementById("fecha_inicio_trabajo").value;
    const fecha_fin_trabajo = document.getElementById("fecha_fin_trabajo").value;

    //COMPROBAMOS LA LONGITUD DE LOS CAMPOS NOMBRE, APELLIDOS - MIKEL
    if(nombre.length < 2){
        alert("Nombre incorrecto");
        return false;
    }

    if(apellidos.length < 2){
        alert("Apellidos incorrectos");
        return false;
    }

    //COMPROBAMOS QUE EL DNI TENGA AL MENOS 9 CARACTERES - XABIER
    if (DNI.length < 9) {
        alert("DNI incorrecto. El DNI debe tener al menos 9 caracteres.");
        return false;
    }

    // COMPROBAMOS QUE EL TELÉFONO TENGA AL MENOS 9 DÍGITOS - XABIER
    if (telefono.length < 9) {
        alert("Teléfono incorrecto. Debe tener al menos 9 dígitos.");
        return false;
    }

     // VALIDAMOS FECHAS DE FORMACIÓN ACADÉMICA Y EXPERIENCIA LABORAL - ASIER
    if(fecha_fin_estudios < fecha_inicio_estudios){
        alert("Fecha de finalización de estudios incorrecta");
        return false;
    }

    if(fecha_fin_trabajo < fecha_inicio_trabajo){
        alert("Fecha de finalización del trabajo incorrecta");
        return false;
    }

    // COMPROBAMOS QUE EL EMAIL CONTENGA UNA @  - JARA
    if (correo_electronico.includes("@") == false) {
        alert("Email incorrecto. Debe contener una @.");
        return false;
    }

    // COMPROBAMOS QUE EL EMAIL CONTENGA UN PUNTO - JARA
    if (correo_electronico.includes(".") == false) {
        alert("Email incorrecto. Debe contener un punto.");
        return false;
    }

    //ALERTAMOS CON UN MENSAJE DE CONFIRMACIÓN
    alert("¡Perfecto! Tus datos se han validado correctamente.");
    return true;
}