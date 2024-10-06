#!/usr/bin/python3
import pickle
"""
Este módulo permite serializar y deserializar objetos con el módulo Pickle.
"""

class CustomObject:
    """
    Clase que representa un objeto personalizado.
    Incluye métodos para serializar y deserializar con el módulo pickle.
    """
    def __init__(self, name, age, is_student):
        """
        Inicializa un nuevo objeto CustomObject.

        Parámetros:
        name (str): El nombre de la persona.
        age (int): La edad de la persona.
        is_student (bool): Indica si la persona es estudiante.
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

        Parámetros:
        filename (str): El nombre del archivo donde se guardará el objeto serializado.
        """
        try:
            with open(filename, "wb") as archivo:
                pickle.dump(self, archivo)
        except (OSError, IOError) as e:
            print(f"Error al escribir el archivo: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Carga y deserializa un objeto desde un archivo utilizando pickle.
        """
        try:
            with open(filename, "rb") as archivo:
                contenido = pickle.load(archivo)
                return contenido
        except (OSError, IOError) as e: #Error de escritura o lectura
            return None
        except pickle.UnpicklingError as e: #En otro formato o corrupto
            return None
