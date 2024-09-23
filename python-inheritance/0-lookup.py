#!/usr/bin/python3
"""
lookup(obj): Devuelve una lista de atributos y métodos disponibles de un objeto.

Parámetros:
- obj: El objeto cuyo conjunto de atributos y métodos se desea obtener.

Retorna:
- Una lista de nombres que representan los atributos y métodos disponibles del objeto proporcionado.
"""

def lookup(obj):
    """
    Devuelve una lista de atributos y métodos disponibles para el objeto dado.

    Parámetros:
    - obj: El objeto cuyo conjunto de atributos y métodos se desea consultar.

    Retorna:
    - lista: Una lista de cadenas que representan los nombres de los atributos y métodos.
    """
    lista = dir(obj)
    return lista