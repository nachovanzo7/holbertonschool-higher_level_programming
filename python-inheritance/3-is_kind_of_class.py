#!/usr/bin/python3
"""
Este módulo contiene una función que verifica si un objeto es una instancia,
o una instancia heredada, de una clase especificada.

Funciones:
    is_kind_of_class(obj, a_class): Retorna True si el objeto es una instancia 
    de la clase especificada o de una subclase, de lo contrario retorna False.
"""

def is_kind_of_class(obj, a_class):
    """
    Verifica si el objeto 'obj' es una instancia o una instancia heredada 
    de la clase 'a_class'.
    
    Args:
        obj: El objeto a verificar.
        a_class: La clase contra la que se compara el objeto.
    
    Returns:
        True si 'obj' es una instancia de 'a_class' o de una subclase,
        False en cualquier otro caso.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
