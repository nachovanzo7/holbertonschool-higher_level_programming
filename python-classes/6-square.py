#!/usr/bin/python3
"""
Este modulo creará una funcion Square
"""
class Square:
    """
    Esta funcion le asigna un valor al atributo inicializado en 0
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or not all(isinstance(i, int) for i in tupla) or not all(i > 0 for i in tupla):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__size):
                if not self.__position[1] > 0:
                    for x in range(self.__position[0]):
                        print("_", end="")
                else:
                    for x in range(self.__position[0]):
                        print(" ", end ="")

                for x in range(self.__size):
                    print("#", end="")
                    if x == self.__size:
                        print("")
                print("")
            

    def area(self):
        return self.__size * self.__size
