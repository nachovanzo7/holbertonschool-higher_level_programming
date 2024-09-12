#!/usr/bin/python3
def uniq_add(my_list=[]):
    lista = []
    sum = 0
    for x in my_list:
        if x not in lista:
            lista.append(x)
    for x in lista:
        sum += x
    return sum
