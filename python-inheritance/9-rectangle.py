#!/usr/bin/python3

"""
Módulo que define la clase BaseGeometry.

Este módulo contiene la clase BaseGeometry, que sirve como clase base
para formas geométricas. Actualmente, es una clase vacía, pero puede ser
extendida con métodos y atributos específicos en el futuro.
"""

class BaseGeometry:
    """
    Clase base para formas geométricas.

    Esta clase está diseñada para ser una clase base de la cual se pueden 
    derivar otras clases que representen formas geométricas. Actualmente,
    no contiene métodos ni atributos.
    """

    def area(self):
        return self.width * self.height

    def integer_validator(self, name, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Clase que representa un rectángulo, hereda de BaseGeometry.
    
    Args:
        width (int): Ancho del rectángulo.
        height (int): Altura del rectángulo.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
