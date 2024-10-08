#!/usr/bin/python3
"""
Este modulo creará una funcion Square
"""
class Square:
    """
    Esta funcion le asigna un valor al atributo inicializado en 0
    """
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
