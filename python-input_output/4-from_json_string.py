#!/usr/bin/python3
"""
Este módulo proporciona una función para convertir una cadena de texto en formato
JSON a su correspondiente objeto de Python.
"""

import json

def from_json_string(my_str):
    """
    Convierte una cadena en formato JSON a un objeto de Python.

    Args:
        my_str (str): Cadena de texto en formato JSON.

    Returns:
        obj: Objeto de Python correspondiente a la cadena JSON.

    Raises:
        json.JSONDecodeError: Si la cadena no está en un formato JSON válido.
    """
    return json.loads(my_str)