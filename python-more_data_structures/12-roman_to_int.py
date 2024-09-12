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
    rom = 0
    sum = 0
    ban = 1
    if not type(roman_string) is str or roman_string is None:
        return 0
    else:
        for x in roman_string:
            if ban == 1:
                rom = romanos.get(x)
                ban += 1

            if (rom >= romanos.get(x)):
                sum += romanos.get(x)
            else:
                sum -= romanos.get(x)
            rom = romanos.get(x)
    return abs(sum)
