#!/usr/bin/python3
"""
lookup(obj): Devuelve lista de atributos y métodos disponibles de un objeto

Parámetros:
- obj: El objeto cuyo conjunto de atributos y métodos se desea obtener.

Retorna:
-Lista de nombres que representan atributos y métodos disponibles del objeto
"""


def lookup(obj):
    """
    Devuelve una lista de atributos y métodos disponibles para el objeto dado.

    Parámetros:
    -obj: El objeto cuyo conjunto de atributos y métodos se desea consultar.

    Retorna:
    -lista: lista de cadenas que representan nombres de atributos y métodos
    """
    lista = dir(obj)
    return lista
