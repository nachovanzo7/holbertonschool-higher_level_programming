#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lista = [None] * len(my_list)
    i = 0
    for x in my_list:
        if (x % 2 == 0):
            lista[i] = True
            i += 1
        else:
            lista[i] = False
            i += 1
    return lista
