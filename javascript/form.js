//AUTOR: JARA, MIKEL, ASIER, XABIER
//JAVASCRIPT PARA FORM_CV.HTML

//FUNCIÓN PARA VALIDAR FORMULARIO
function validarFormulario(event) {

    //EVITAMOS QUE LA PÁGINA SE RECARGUE
    //JARA: LOS BUSQUE EN INTERNET PORQUE NO PODIA COMPROBAR LOS DATOS EN LA CONSOLA Y ME DECIA DE PONER ESTO
    event.preventDefault();

    //RECOGEMOS LOS DATOS DEL USUARIO
    const nombre = document.getElementById("nombre").value;
    const apellidos = document.getElementById("apellidos").value;
    const DNI = document.getElementById("DNI").value;
    const correo_electronico = document.getElementById("correo_electronico").value;
    const telefono = document.getElementById("telefono").value;
    const direccion = document.getElementById("direccion").value;


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

    // RECOGEMOS LOS DATOS DE HABILIDADES
    const softskills = document.querySelectorAll('input[name="softskills"]:checked');
    const otras_softskills = document.getElementsByName("otras_softskills")[0].value;
    const softwares = document.querySelectorAll('input[name="softwares"]:checked');
    const otros_softwares = document.getElementsByName("otros_softwares")[0].value;
    const idioma = document.getElementById("idioma").value;
    const nivel_idioma_seleccionado = document.querySelector('input[name="nivel_idioma"]:checked');
    const nivel_idioma = nivel_idioma_seleccionado ? nivel_idioma_seleccionado.value : "";

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

    //MOSTRAMOS LOS DATOS EN LA CONSOLA
    console.log("----- INFORMACIÓN PERSONAL -----");
    console.log("Nombre:", nombre);
    console.log("Apellidos:", apellidos);
    console.log("DNI:", DNI);
    console.log("Correo electrónico:", correo_electronico);
    console.log("Teléfono:", telefono);
    console.log("Dirección:", direccion);

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

    console.log("----- HABILIDADES -----");
    console.log("Softskills seleccionadas:", Array.from(softskills).map(opcion => opcion.value));
    console.log("Otras softskills:", otras_softskills);
    console.log("Softwares seleccionados:", Array.from(softwares).map(opcion => opcion.value));
    console.log("Otros softwares:", otros_softwares);
    console.log("Idioma seleccionado:", idioma);
    console.log("Nivel de idioma:", nivel_idioma);

    //ALERTAMOS CON UN MENSAJE DE CONFIRMACIÓN
    alert("¡Perfecto! Tus datos se han validado correctamente.");
    return true;
}