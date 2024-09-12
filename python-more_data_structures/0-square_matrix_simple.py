#!/usr/bin/python3
def square(x):
    return x * x

def square_matrix_simple(matrix=[]):
    resultado = []
    for fila in matrix:
        resultado.append(list(map(square, fila)))
    return resultado
