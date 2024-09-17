#!/usr/bin/python3
"""
Este módulo creará una clase Rectangle.
"""
class Rectangle:
    """
    Esta clase define un atributo Rectangulo.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            if not type(value) is int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__width = value
        except (TypeError, ValueError) as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if not type(value) is int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__height = value
        except (TypeError, ValueError) as e:
            print("[{}] {}".format(e.__class__.__name__, e))