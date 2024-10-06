#!/usr/bin/python3
"""
Este módulo con función para convertir los atributos a un diccionario.
"""


def class_to_json(obj):
    """
    Parámetros:
        obj (object): La instancia de la clase cuyo contenido 
        se convertirá a un diccionario.

    Retorno:
        dict: Un diccionario que contiene los atributos del objeto.
    """
    return obj.__dict__
