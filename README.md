# TALENT CONNECT

## Descripción del proyecto

TalentConnect es un proyecto que consiste en crear una plataforma de empleo. A través de ella, los usuarios pueden consultar ofertas de trabajo, subir su CV y conocer diferentes empresas desde distintas páginas conectadas entre sí.

## Funcionamiento de la página web

La página principal es **`PaginaWeb.html`**. Desde ella se puede navegar al resto de páginas del proyecto utilizando el menú superior y los enlaces que aparecen en las diferentes secciones.

El proyecto cuenta con tres páginas principales además de la página de inicio:

- **`empleos.html`**: contiene las ofertas de trabajo disponibles para que los usuarios puedan consultar las distintas vacantes.

- **`empresas.html`**: incluye información sobre las empresas colaboradoras y aquellas que ofrecen oportunidades laborales a través de TalentConnect.

- **`form_cv.html`**: contiene un formulario para introducir datos personales, académicos y profesionales y enviar el currículum.

## Diseño y estilos - `Estilos.css`

Para dar formato y diseñar las diferentes páginas de TalentConnect, hemos utilizado una hoja de estilos CSS externa llamada `Estilos.css`, que se encuentra dentro de la carpeta `style`.

```html
<link rel="stylesheet" href="style/Estilos.css">
```

Desde este archivo se controlan aspectos visuales como:

- Los colores y fondos de la página.
- Los tamaños y estilos de los textos.
- La distribución de los elementos mediante Flexbox.
- El diseño del menú de navegación.
- La apariencia de las tarjetas y sus efectos al pasar el ratón por encima.
- Los márgenes, espacios y tamaños de las diferentes secciones.
- etc...

De esta manera, mantenemos el código HTML separado de los estilos CSS, lo que facilita la organización y modificación del diseño de la página web.

## Imágenes y recursos - `assets`

El proyecto cuenta con una carpeta `assets` destinada a almacenar las imágenes y otros recursos gráficos utilizados en la página web, como el logo y la imagen de portada.

## Página Principal - `PaginaWeb.html`

La página principal está dividida en diferentes apartados:

### 1. Header y menú de navegación

En la parte superior encontramos el logo de TalentConnect y un menú con cuatro pestañas interactivas:

- **Empleos**: permite acceder a la página de ofertas de empleo.

- **Subir CV**: dirige a un formulario para adjuntar el CV.

- **Empresas**: permite acceder a una página con información sobre las empresas.

- **Contáctanos**: en un futuro permitirá dirigirse una sección para mandar mensajes.

### 2. Portada principal

La portada contiene una imagen de fondo con un mensaje de bienvenida y el eslogan de la página:

«Tu Gestor de Talento Inteligente»

### 3. Información general y contacto

Esta sección está dividida en dos partes:

- **Quiénes somos**: presenta TalentConnect, explica el propósito de la plataforma y su función.

- **Datos de contacto**: muestra la dirección de nuestra oficina, el teléfono y el correo electrónico.

### 4. Servicios que ofrecemos

En este apartado aparecen tres tarjetas organizadas mediante Flexbox. Cada una representa uno de los servicios principales de la página:

- **Buscar empleo**: acceso a las ofertas de trabajo.

- **Subir CV**: acceso al formulario del currículum.

- **Empresas**: acceso a la información sobre las empresas colaboradoras.

Las tarjetas tienen enlaces para navegar a sus respectivas páginas y un pequeño efecto visual que se activa al pasar el ratón por encima.

### 5. Footer

En la parte inferior de la página se encuentra el footer, que incluye el nombre de TalentConnect, una frase representativa de la empresa y el aviso de copyright con los derechos reservados.

## Página CV - `form_cv.html`

Esta página contiene un formulario para que los usuarios puedan introducir sus datos personales y comenzar a crear su CV.

Al igual que en la página principal, cuenta con un encabezado que incluye el logo de TalentConnect y el menú de navegación para acceder al resto de páginas.

También, cuenta con una pequeña introducción donde podemos ver el titulo acompañado de un pequeño texto.

### 1. Datos personales
Este formulario recoge información necesaria para elaborar un CV. Incluye los siguientes campos:

- **Nombre**: `type="text"`

- **Apellidos**: `type="text"`

- **Correo**: `type="email"`

- **Telefono**: `type="tel"`

- **Ciudad**: `type="text"`

### 2. Formación académica

En este apartado se recoge la información relacionada con los estudios del usuario. Incluye campos como:

- **Nivel de estudios**: `<select>`

- **Estudios realizados**: `type="text"`

- **Centro educativo**: `type="text"`

- **Año de inicio y finalización**: `type="date"`

### 3. Experiencia laboral

Este apartado permite añadir información sobre los trabajos que ha realizado el usuario anteriormente. Incluye:

- **Puesto de trabajo**: `type="text"`

- **Empresa**: `type="text"`

- **Fecha inicio/fin**: `type="date"`

- **Descripción del puesto**: `<textarea>`

### 4. Habilidades

En este último apartado se recogen las capacidades y conocimientos del usuario. Se divide en diferentes categorías:

- **Softskills**: `type="checkbox"`

- **Softwares**: `type="checkbox"`

- **Idiomas**: `<select>`

- **Nivel de idiomas**: `type="radio"`

### Botón de envío

Al final del formulario encontramos el botón «ENVIAR» y al pulsarlo se ejecuta la función javascript encargada de validar el formulario.

## JavaScript - `form.js`

Para añadir funcionalidad al formulario hemos creado un archivo javascript externo llamado `form.js`, que se encuentra dentro de la carpeta `javascript`.

Este archivo está vinculado al documento html mediante la etiqueta script, situada al final del body.

```html
<script src="javascript/form.js"></script>
```

Hemos desarrollado la función `validarFormulario(event)`, que se ejecuta cuando el usuario pulsa el botón de envío. Dentro de esta función se han añadido diferentes comprobaciones para validar los datos introducidos por el usuario y evitar que se envíe el formulario si alguno de ellos es incorrecto.

Las validaciones realizadas son las siguientes:

- Correo electrónico: se comprueba que la dirección de correo electrónico contenga una arroba (@) y un punto (.).

- Nombre y apellidos: se comprueba que ambos campos tengan una longitud mínima de 2 caracteres.

- DNI: se verifica que el DNI tenga al menos 9 caracteres.

- Teléfono: se comprueba que el número de teléfono tenga al menos 9 dígitos.

-Fechas: se verifica que la fecha de inicio sea anterior a la fecha de finalización.

Si alguno de estos datos no cumple las condiciones establecidas, se muestra una alerta indicando el error y se devuelve false, impidiendo que el formulario se envíe.

De esta manera, conseguimos que los datos introducidos por el usuario cumplan unos requisitos mínimos antes de procesar el envío del formulario.

## `empresas.html` y `empleos.html`
Ambas páginas están destinadas a mostrar las ofertas de trabajo disponibles y la información sobre las empresas colaboradoras de TalentConnect.

Por el momento, hemos añadido en las dos páginas el encabezado (header), que incluye el logo y el menú de navegación, manteniendo la misma estética que en el resto del proyecto.

Además, hemos incorporado un mensaje de «COMING SOON» en grande para indicar que ambas secciones estarán disponibles próximamente.