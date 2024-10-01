#!/usr/bin/python3
"""
Este módulo contiene una función para leer el contenido de un archivo de texto y
mostrarlo en la salida estándar.
"""

def read_file(filename=""):
    """
    Lee el contenido de un archivo de texto y lo imprime en la salida estándar.

    Args:
        filename (str): Nombre del archivo que se va a leer. El valor predeterminado
        es una cadena vacía, lo que significa que se debe especificar un archivo.

    Raises:
        FileNotFoundError: Si el archivo especificado no existe o no se puede encontrar.
        UnicodeDecodeError: Si ocurre un error al decodificar el contenido del archivo.
    """
    with open(filename, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
        print("{}\n".format(texto))