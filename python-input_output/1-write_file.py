#!/usr/bin/python3
"""
Modulo para utilizar Python
"""
def write_file(filename="", text=""):
    """
    Funcion que escribe dentro de un archivo
    y retorna la cantidad de caracteres escritas
    """
    if (filename is not None):
        with open(filename, "w", encoding="utf-8") as archivo:
            len = archivo.write(text)
    else:
        with open(filename, "a", encoding="utf-8") as archivo:
            len = archivo.write(text)
    return len
