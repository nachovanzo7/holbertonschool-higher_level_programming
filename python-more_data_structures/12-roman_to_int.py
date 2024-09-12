#!/usr/bin/python3
def roman_to_int(roman_string):
    romanos = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    }

    if not type(roman_string) is str or roman_string is None:
        return 0
    total = 0
    rom = 0

    for char in reversed(roman_string):
        value = romanos.get(char, 0)
        if value >= rom:
            total += value
        else:
            total -= value
        rom = value

    return total