#!/usr/bin/python3

import json
"""
Modulo para poder utilizar todas las funciones json
"""

def serialize_and_save_to_file(data, filename):
    """
    Serializa los datos proporcionados en formato JSON y los guarda en un archivo.
    Parametros:
    data - diccionario Python
    filename - archivo para almacenar datos
    """
    with open(filename, "w") as archivo:
        json.dump(data, archivo)

def load_and_deserialize(filename):
    """
    Carga y deserializa los datos contenidos en el archivo
    Return: retorna un diccionario Python
    """
    with open(filename, "r") as archivo:
        contenido = json.load(archivo)
    return contenido
