#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for fila in range(len(matrix)):
            for x in range(len(matrix[fila])):
                if x < len(matrix[fila]) - 1:
                    print("{:d} ".format(matrix[fila][x]), end="")
                else:
                    print("{:d}".format(matrix[fila][x]), end="")
            print()
