#!/usr/bin/python3
"""
Modulo para python
"""
def append_write(filename="", text=""):
    """
    Concatena texto en archivo
    si no existe lo crea
    """
    with open(filename, "w") as archivo:
        len = archivo.write(text)
        return len