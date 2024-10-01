#!/usr/bin/python3
"""
Este módulo proporciona una función para guardar un objeto de Python en un archivo
en formato JSON.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Guarda un objeto de Python en un archivo en formato JSON.

    Args:
        my_obj (any): El objeto de Python a guardar. Puede ser cualquier estructura
        serializable en JSON (listas, diccionarios, etc.).
        filename (str): Nombre del archivo en el que se guardará el objeto.

    Raises:
        TypeError: Si el objeto no es serializable en JSON.
    """
    with open(filename, "w", ) as archivo:
        archivo.write(json.dumps(my_obj))
