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

Inicialmente, las imágenes estaban guardadas en local en formatos como PNG y JPG. Sin embargo, al abrir la página desde otro equipo, algunas imágenes no se mostraban correctamente porque los archivos no estaban disponibles en ese otro dispositivo.

Para solucionar este problema, decidimos subir las imágenes a **Cloudinary**, una plataforma de almacenamiento y gestión de imágenes. De esta manera, podemos utilizarlas mediante enlaces URL directamente en el código HTML, evitando depender de archivos almacenados únicamente en nuestro equipo.

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

## Página Empleos - `empleos.html`

Texto

## Página CV - `form_cv.html`

Texto

## Página Empresa - `empresas.html`

Texto