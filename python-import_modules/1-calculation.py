#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(str(a), str(b), add(a, b)))
    print("{} - {} = {}".format(str(a), str(b), sub(a, b)))
    print("{} * {} = {}".format(str(a), str(b), mul(a, b)))
    print("{} / {} = {}".format(str(a), str(b), div(a, b)))
