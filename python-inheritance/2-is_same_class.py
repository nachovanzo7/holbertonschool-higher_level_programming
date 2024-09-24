#!/usr/bin/python3
"""
Este módulo contiene una función que verifica si un objeto es exactamente
una instancia de una clase especificada.

Funciones:
    is_same_class(obj, a_class): Retorna True si el objeto es exactamente
    una instancia de la clase especificada, de lo contrario retorna False.
"""

def is_same_class(obj, a_class):
    """
    Verifica si el objeto 'obj' es exactamente una instancia de la clase 'a_class'.
    
    Args:
        obj: El objeto a verificar.
        a_class: La clase contra la que se compara el objeto.
    
    Returns:
        True si 'obj' es exactamente una instancia de 'a_class',
        False en cualquier otro caso (incluidas subclases).
    """
    if type(obj) == a_class:
        return True
    else:
        return False
