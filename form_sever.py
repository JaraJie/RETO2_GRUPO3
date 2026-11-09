from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from html import escape

class Handler(BaseHTTPRequestHandler):

    # Respuesta cuando se accede desde el navegador (GET)
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        respuesta = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>TalentConnect</title>
        </head>
        <body>
            <h1>Servidor funcionando correctamente</h1>
            <p>El servidor está esperando que envíes el formulario mediante POST.</p>
        </body>
        </html>
        """

        self.wfile.write(respuesta.encode("utf-8"))

    # Recibir los datos del formulario
    def do_POST(self):

        # Leemos los datos enviados
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length).decode("utf-8")

        # Organizamos los datos recibidos
        form = parse_qs(data)

        # Mostramos los datos en la terminal
        print("\n--- NUEVO CV RECIBIDO ---")
        for campo, valor in form.items():
            print(f"{campo}: {valor}")

        # Obtenemos el nombre del usuario
        nombre = escape(form.get("nombre", ["Usuario"])[0])

        # Preparamos la respuesta HTML
        respuesta = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>TalentConnect</title>
        </head>
        <body>
            <h1>¡Formulario enviado correctamente!</h1>
            <p>Gracias, <strong>{nombre}</strong>.</p>
            <p>TalentConnect ha recibido tus datos.</p>
        </body>
        </html>
        """

        # Enviamos la respuesta
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(respuesta.encode("utf-8"))


# Iniciamos el servidor
print("Servidor iniciado en http://localhost:8000")
HTTPServer(("localhost", 8000), Handler).serve_forever()