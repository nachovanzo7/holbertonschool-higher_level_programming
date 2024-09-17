#!/usr/bin/python3
"""
Este módulo creará una clase Rectangle.
"""
class Rectangle:
    """
    Esta clase define un atributo Rectangulo.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            if not type(value) is int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
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
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        except (TypeError, ValueError) as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
