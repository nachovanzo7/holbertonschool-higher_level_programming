#!/usr/bin/python3
"""
Este módulo proporciona una función para guardar un objeto de Python en un archivo
en formato JSON.
"""
import json

def load_from_json_file(filename):
    """
    Carga un objeto desde un archivo JSON.

    Args:
        filename (str): El nombre del archivo JSON desde el cual se va a cargar el objeto.

    Returns:
        objeto: El objeto Python representado por los datos JSON contenidos en el archivo.
    
    Excepciones:
        FileNotFoundError: Si el archivo no existe.
        json.JSONDecodeError: Si el contenido del archivo no es un JSON válido.
    
    Ejemplo:
        objeto = load_from_json_file("archivo.json")
    """
    with open(filename, 'r', encoding='utf-8') as archivo:
        objeto = json.load(archivo)  # Carga el contenido JSON desde el archivo
        return objeto