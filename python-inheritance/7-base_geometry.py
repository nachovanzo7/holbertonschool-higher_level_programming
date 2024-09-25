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
        if (self.area):
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
  