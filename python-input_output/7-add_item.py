#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Este script agrega todos los argumentos pasados por línea de comandos
a una lista, luego guarda dicha lista en un archivo JSON.
- Si el archivo ya existe, se carga su contenido
- Si el archivo no existe, se crea uno nuevo con los argumentos.

Módulos:
    sys: Proporciona acceso a argumentos pasados desde la línea de comandos.
    json: Módulo estándar de Python para trabajar con datos en formato JSON.
    os.path: Módulo que contiene funciones para manipular rutas de archivos.
    save_to_json_file: Función que guarda datos en un archivo JSON.
    load_from_json_file: Función que carga datos de un archivo JSON.

Archivos:
    add_item.json: se almacenan los elementos en formato JSON.
"""

import sys
import json
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

if path.exists(filename):  # Si el archivo existe, carga su contenido
    item = load_from_json_file(filename)
else:
    item = []  # Si no existe, crea una nueva lista

# Agrega los argumentos pasados por línea de comandos a la lista
item.extend(sys.argv[1:])

# Guarda la lista actualizada en el archivo JSON
save_to_json_file(item, filename)