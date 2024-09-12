#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    copia = my_list[:]
    for x in my_list:
        if x == search:
            copia[i] = replace
            i += 1
        else:
            i += 1
    return copia
