#!/usr/bin/python3

"""
Módulo que contiene la función para generar el Triángulo de Pascal.
"""


def pascal_triangle(n):
    """
    Genera el Triángulo de Pascal hasta la fila n.

    Parámetros:
        n (int): El número de filas del Triángulo de Pascal a generar.
                  Si n es menor o igual a 0, devuelve una lista vacía.

    Retorno:
        list: Una lista que contiene las filas del Triángulo de Pascal, 
               donde cada fila es una lista de enteros.
    """
    list = []
    if n <= 0:
        return list

    for i in range(n):
        fila = [1] * (i + 1)

        for x in range(1, i): #menos las puntas, se suman los nums anteriores
            fila[x] = (list[i - 1][x - 1]) + (list[i - 1][x])

        list.append(fila)

    return list
