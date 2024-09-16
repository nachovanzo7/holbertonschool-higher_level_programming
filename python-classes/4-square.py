#!/usr/bin/python3
"""
Este modulo creará una funcion Square
"""
class Square:
    """
    Esta funcion le asigna un valor al atributo inicializado en 0
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError ("size must be an integer")
        elif value < 0:
            raise ValueError ("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
