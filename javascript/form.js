//AUTOR: JARA
//JAVASCRIPT PARA FORM_CV.HTML

//FUNCIÓN PARA VALIDAR FORMULARIO
function validarFormulario(event) {

    //EVITAMOS QUE LA PÁGINA SE RECARGUE
    //JARA: LOS BUSQUE EN INTERNET PORQUE NO PODIA COMPROBAR LOS DATOS EN LA CONSOLA Y ME DECIA DE PONER ESTO
    event.preventDefault();

    //RECOGEMOS LOS DATOS DEL USUARIO
    const nombre = document.getElementById("nombre").value;
    const apellidos = document.getElementById("apellidos").value;

    // RECOGEMOS LOS DATOS DE FORMACIÓN ACADÉMICA
    const nivel_estudios = document.getElementById("nivel_estudios").value;
    const estudios = document.getElementById("estudios").value;
    const centro = document.getElementById("centro").value;
    const fecha_inicio_estudios = document.getElementById("fecha_inicio_estudios").value;
    const fecha_fin_estudios = document.getElementById("fecha_fin_estudios").value;

    // RECOGEMOS LOS DATOS DE EXPERIENCIA LABORAL
    const puesto = document.getElementById("puesto").value;
    const empresa = document.getElementById("empresa").value;
    const fecha_inicio_trabajo = document.getElementById("fecha_inicio_trabajo").value;
    const fecha_fin_trabajo = document.getElementById("fecha_fin_trabajo").value;
    const descripcion = document.getElementById("descripcion").value;

    //MOSTRAMOS LOS DATOS EN LA CONSOLA
    console.log("----- INFORMACIÓN PERSONAL -----");
    console.log("Nombre:", nombre);
    console.log("Apellidos:", apellidos);

    console.log("----- FORMACIÓN ACADÉMICA -----");
    console.log("Nivel de estudios:", nivel_estudios);
    console.log("Estudios realizados:", estudios);
    console.log("Centro educativo:", centro);
    console.log("Fecha de inicio:", fecha_inicio_estudios);
    console.log("Fecha de finalización:", fecha_fin_estudios);

    console.log("----- EXPERIENCIA LABORAL -----");
    console.log("Puesto de trabajo:", puesto);
    console.log("Empresa:", empresa);
    console.log("Fecha de inicio:", fecha_inicio_trabajo);
    console.log("Fecha de finalización:", fecha_fin_trabajo);
    console.log("Descripción del puesto:", descripcion);

    //ALERTAMOS CON UN MENSAJE DE CONFIRMACIÓN
    alert("¡Perfecto! Tus datos se han validado correctamente.");

}

//RECORDAD Y PONER LOS DEMÁS DATOS PARA QUE SE GUARDE EN CONSOLA
//CREAR FUNCIONES PARA QUE LOS CAMPOS NO ESTEN VACIOS Y QUE ALERTE
//OTRAS FUNCIONES COMO LAS HEMOS HECHO EN CLASE DE QUE EL NOMBRE TENGA 3 CARÁCTERES POR LO MENOS