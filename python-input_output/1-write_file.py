#!/usr/bin/python3

def write_file(filename="", text=""):
    if (filename is not None):
        with open(filename, "w", encoding="utf-8") as archivo:
            len = archivo.write(text)
    else:
        with open(filename, "a", encoding="utf-8") as archivo:
            len = archivo.write(text)
    return len
