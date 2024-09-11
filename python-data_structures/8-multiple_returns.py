#!/usr/bin/python3
def multiple_returns(sentence):
    long = 0
    if sentence == "":
        car = None
    else:
        long = len(sentence)
        car = sentence[0]
    tupla = (long, car)
    return tupla
