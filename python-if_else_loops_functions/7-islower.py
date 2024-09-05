#!/usr/bin/python3

def islower(c):
    if (ord(c) >= 97 and ord(c) <= 122):
        return True
    elif (c.isdigit()):
        return False
    else:
        return False
