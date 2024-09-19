#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide cada elemento de una matrix por un divisor dado y 
    redondea el resultado a 2 decimales.

    Parámetros:
    matrix (lista de listas de int/float): Una matriz (lista de listas) donde cada elemento es un entero o flotante.
    div (int/float): El número por el cual se dividirá cada elemento de la matriz.

    Retorna:
    lista de listas de float: Una nueva matriz con cada elemento dividido por `div` y redondeado a 2 decimales.

    Excepciones:
    TypeError: Si `matrix` no es una lista de listas de enteros o flotantes.
    TypeError: Si `div` no es un entero o flotante.
    ZeroDivisionError: Si `div` es cero.
    TypeError: Si cada fila en `matrix` no tiene el mismo tamaño.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    longitud = len(matrix[0])
    if not all(len(fila) == longitud for fila in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    aux_matrix = []
    for fila in matrix:
        aux_fila = []
        for x in fila:
            aux_fila.append(round(x / div, 2))  # Redondear a 2 decimales
        aux_matrix.append(aux_fila)

    return aux_matrix