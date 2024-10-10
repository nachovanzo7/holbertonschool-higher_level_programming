#!/usr/bin/python3 

import http.server
from http.server import HTTPServer

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        self.wfile.write(b"Bienvenidos a Yugoslavia")

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
httpd.serve_forever()

