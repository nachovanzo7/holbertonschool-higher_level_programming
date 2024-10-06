#!/usr/bin/python3
"""
Este módulo define una clase `Student` con atributos:
primer nombre, apellido y edad. Además, incluye un método para
convertir los atributos del estudiante a un diccionario.
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
        self.first_name = first_name  # Asigna el primer nombre al atributo
        self.last_name = last_name  # Asigna el apellido al atributo
        self.age = age  # Asigna la edad al atributo

    def to_json(self, attrs=None):
        """
        Devuelve un diccionario que representa los atributos del estudiante.

        Si se proporciona una lista de atributos (attrs), solo se incluyen
        esos atributos en el diccionario de salida.

        Parámetros:
            attrs (list, opcional): Lista de cadenas que representan los nombres
            de los atributos a incluir en el diccionario. Si es None, se
            incluirán todos los atributos.

        Retorno:
            dict: Un diccionario que contiene los atributos especificados
            o todos los atributos del estudiante.
        """
        resultado = {}

        if attrs is not None:
            for atributo in attrs:
                if hasattr(self, atributo):
                    resultado[atributo] = getattr(self, atributo)
            return resultado

        return self.__dict__
    def reload_from_json(self, json):
        """
        Actualiza los atributos de la instancia de Student

        Parámetros:
            json (dict): Un diccionario que contiene los nuevos valores
            para los atributos `first_name`, `last_name` y `age`.
        """
        self.first_name = json.get("first_name")
        self.last_name = json.get("last_name")
        self.age = json.get("age")
