// AUTOR: JARA
// JAVASCRIPT PARA FORM_CV.HTML

function validarFormulario(event) {

    const nombre = document.getElementById("nombre").value.trim();
    const apellidos = document.getElementById("apellidos").value.trim();

    console.log("Nombre:", nombre);
    console.log("Apellidos:", apellidos);

    alert("¡Perfecto! Tus datos se han validado correctamente.");

}