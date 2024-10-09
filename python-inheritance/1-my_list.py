#!/usr/bin/python3
"""
Modulo para utilizar python
"""


class MyList(list):
    """
    Herencia de list e imprime una lista
    """
    def print_sorted(self):
        print(sorted(self))
