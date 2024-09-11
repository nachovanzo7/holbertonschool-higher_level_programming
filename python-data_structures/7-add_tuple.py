#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) >= 2 and len(tuple_a) >= 2:
        tupla = ((tuple_a[0] + tuple_b[0], (tuple_a[1] + tuple_b[1])))
    elif len(tuple_b) == 1:
        tupla = ((tuple_a[0] + tuple_b[0], (tuple_a[1])))
    elif len(tuple_a <= 2)
    else:
        tupla = tuple_a
    return (tupla)
