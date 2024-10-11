#!/usr/bin/python3

import http.server
from http.server import HTTPServer
import json

# Clase personalizada para manejar solicitudes GET
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":    
            # Enviar respuesta 200 (OK)
            self.send_response(200)
            
            # Enviar los encabezados necesarios
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            # Enviar el contenido de la respuesta
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York" 
            }
            self.send_response(200)
        
            # Enviar los encabezados necesarios
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            # Enviar el contenido de la respuesta
            self.wfile.write(json.dumps(data).encode('utf-8'))
            
        elif self.path == "/status":    
            # Enviar respuesta 200 (OK)
            self.send_response(200)
            
            # Enviar los encabezados necesarios
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            # Enviar el contenido de la respuesta
            self.wfile.write(b"OK")
            
        elif self.path == "/info":    
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.send_response(200)
        
            # Enviar los encabezados necesarios
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            # Enviar el contenido de la respuesta
            self.wfile.write(json.dumps(data).encode('utf-8'))
            
        else:   
            # Enviar respuesta 200 (OK)
            self.send_response(404)
            
            # Enviar los encabezados necesarios
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()

            # Enviar el contenido de la respuesta
            self.wfile.write(b"Endpoint not found")
            
        

# Dirección del servidor: ('', 8000) escucha en el puerto 8000
server_address = ('', 8000)

# Instancia del servidor
httpd = HTTPServer(server_address, MyHandler)

try:
    # Mensaje de confirmación de que el servidor está corriendo
    print("Servidor corriendo en el puerto 8000...")
    
    # Ejecutar el servidor
    httpd.serve_forever()

except KeyboardInterrupt:
    # Si se presiona Ctrl+C, se cerrará el servidor limpiamente
    print("\nServidor detenido.")
    httpd.server_close()