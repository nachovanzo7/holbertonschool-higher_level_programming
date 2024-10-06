#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Este módulo define una clase `Student` con atributos:
primer nombre, apellido y edad. Además, incluye un método para
convertir los atributos del estudiante a un diccionario
"""


class Student:
    """
    Clase que define a un estudiante.

    Atributos:
        first_name (str): Primer nombre del estudiante.
        last_name (str): Apellido del estudiante.
        age (int): Edad del estudiante.
    """

    def __init__(self, first_name, last_name, age):
        """
        Inicializa una nueva instancia de la clase `Student`.

        Parámetros:
            first_name (str): El primer nombre del estudiante.
            last_name (str): El apellido del estudiante.
            age (int): La edad del estudiante.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Devuelve un diccionario que representa los atributos del estudiante.

        Retorno:
            dict: contiene los atributos `first_name`, `last_name` y `age`.
        """
        return self.__dict__