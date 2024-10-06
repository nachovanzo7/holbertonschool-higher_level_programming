#!/usr/bin/python3
"""
Este módulo define una función para convertir un objeto Python
a una cadena en formato JSON.
"""
import json


def to_json_string(my_obj):
    """
    Convierte un objeto Python en una cadena de texto en formato JSON.

    Parámetros:
        my_obj: El objeto que se desea serializar a JSON.
    Retorno:
        str: Cadena en formato JSON que representa el objeto proporcionado.
    """
    serializado = json.dumps(my_obj)
    return serializado
