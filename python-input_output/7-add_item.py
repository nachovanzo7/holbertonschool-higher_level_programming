#!/usr/bin/python3
"""
Agrega todos los argumentos pasados por línea de comandos
a una lista, luego guarda dicha lista en un archivo JSON.
Si el archivo ya existe, carga su contenido para agregar los nuevos
elementos. Si no existe, crea el archivo.
"""

import sys
import json
from os import path  # Correccion chat-gpt
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

if path.exists(filename):  # Si el archivo existe - carga
    item = load_from_json_file(filename)
else:
    item = []  # Caso de que no exista - creacion

item.extend(sys.argv[1:])  # Recibo argumentos del usuario y concateno

save_to_json_file(item, filename)
