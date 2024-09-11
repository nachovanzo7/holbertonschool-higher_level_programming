#!/usr/bin/python3
def no_c(my_string):
    i = 0
    copia = ""
    for x in my_string:
        if (x != "c" and x != "C"):
            copia += my_string[i]
        i = i + 1
    return copia
