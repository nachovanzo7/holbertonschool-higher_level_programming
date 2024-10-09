#!/usr/bin/python3
"""
Este script permite agregar argumentos pasados por línea de comandos a un archivo JSON.
- Si el archivo `add_item.json` ya existe, su contenido se carga y se añaden los nuevos elementos.
- Si el archivo no existe, se crea una nueva lista que se guarda en el archivo.
"""

import sys
"""
Módulo sys: Proporciona acceso a argumentos de la línea de comandos.
"""

import json
"""
Módulo json: Módulo estándar de Python para manejar datos en formato JSON.
"""

from os import path
"""
Módulo os.path: Funciones para manipular rutas de archivos, incluyendo la verificación de existencia.
"""

from 5-save_to_json_file import save_to_json_file
"""
Función personalizada save_to_json_file: Guarda datos en un archivo JSON.
"""

from 6-load_from_json_file import load_from_json_file
"""
Función personalizada load_from_json_file: Carga datos de un archivo JSON.
"""

# Nombre del archivo JSON donde se guardarán los datos
filename = "add_item.json"

# Verifica si el archivo ya existe
if path.exists(filename):  # Si el archivo existe, carga su contenido
    item = load_from_json_file(filename)
else:
    item = []  # Si no existe, crea una nueva lista

# Agrega los argumentos pasados por línea de comandos a la lista
item.extend(sys.argv[1:])

# Guarda la lista actualizada en el archivo JSON
save_to_json_file(item, filename)
