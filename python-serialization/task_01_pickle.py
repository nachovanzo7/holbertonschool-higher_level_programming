#!/usr/bin/python3
import pickle
"""
Este modulo permite serializar con Pickle
"""


class CustomObject:
    """
    Clase que representa un objeto personalizado.
    Incluye métodos para serializar y deserializar con el módulo pickle.
    """
    def __init__(self, name, age, is_student):
        """
        Inicializa un nuevo objeto CustomObject.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Muestra los atributos del objeto (nombre, edad, y si es estudiante) en la consola.
        """
        print("Name: {}\nAge: {}\nIs Student: {}".format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        Serializa el objeto actual y lo guarda en un archivo utilizando pickle.
        """
        with open(filename, "wb") as archivo:
            pickle.dump(self, archivo)

    @classmethod 
    def deserialize(cls, filename):
        """
        arga y deserializa un objeto desde un archivo
        retorna el objeto deserializado
        """
        with open(filename, "rb") as archivo:
            contenido = pickle.load(archivo)
            return contenido
