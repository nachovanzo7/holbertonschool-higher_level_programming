#!/usr/bin/python3
"""
lookup(obj): Devuelve una lista de atributos y métodos disponibles de un objeto.

Parámetros:
- obj: El objeto cuyo conjunto de atributos y métodos se desea obtener.

Retorna:
- Una lista de nombres que representan los atributos y métodos disponibles del objeto proporcionado.
"""
def lookup(obj):
    lista = dir(obj)
    return lista
