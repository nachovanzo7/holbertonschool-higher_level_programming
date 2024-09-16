#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Suma dos números enteros o flotantes y devuelve un entero.
    
    Requisitos:
    - a o b no son enteros - TypeError.
    - a o b son float - convertir a int antes de sumar
    
    Casos de prueba:
    
    - Suma de dos enteros:
    >>> add_integer(10, 5)
    15
    
    - Suma de un entero y un flotante:
    >>> add_integer(10, 5.9)
    15
    
    - Suma de dos flotantes (se convierten a enteros):
    >>> add_integer(10.1, 5.9)
    15
    
    - Uso del valor por defecto (b=98):
    >>> add_integer(10)
    108
    
    - Errores de tipo: a no es un entero o flotante
    >>> add_integer("10", 5)
    Traceback (most recent call last):
    TypeError: a must be an integer
    
    - Errores de tipo: b no es un entero o flotante
    >>> add_integer(10, "5")
    Traceback (most recent call last):
    TypeError: b must be an integer
    
    - Casos extremos: números negativos
    >>> add_integer(-10, -5)
    -15
    
    - Casos extremos: suma de cero
    >>> add_integer(0, 0)
    0
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Convertir a y b a enteros si son flotantes
    a = int(a)
    b = int(b)
    
    return a + b