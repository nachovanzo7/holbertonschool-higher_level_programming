#!/usr/bin/python3
def uppercase(str):
    imprimir = ""
    for x in str:
        if (ord(x) >= 97 and ord(x) <= 122):
            x = chr(ord(x) - 32)
            imprimir += x
        else:
            imprimir += x
    print(imprimir)
