#!/usr/bin/python3

"""
Módulo que define la función 'inherits_from'.

Este módulo contiene la función 'inherits_from' que verifica si un objeto es
una instancia de una clase que heredó (directa o indirectamente) de la clase 
especificada.

Funciones:
- inherits_from(obj, a_class): Retorna True si 'obj' es una instancia de una 
  clase que hereda de 'a_class', de lo contrario retorna False.
"""

def inherits_from(obj, a_class):
    """
    Verifica si un objeto es una instancia de una clase que heredó (directa o indirectamente)
    de la clase especificada.

    Args:
        obj: El objeto a verificar.
        a_class: La clase a comprobar si es la base de la jerarquía de clases de 'obj'.

    Returns:
        bool: Retorna True si 'obj' es una instancia de una subclase de 'a_class',
              y False si 'obj' es una instancia directa de 'a_class' o no pertenece a la jerarquía.
    """
    if (isinstance(obj, a_class) and not type(obj) == a_class):
        return True  
    else:
        return False  
