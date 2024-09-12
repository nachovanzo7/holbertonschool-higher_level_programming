#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list = a_dictionary.keys()
    list = sorted(list)
    i = 0
    string = ""
    for x in list:
        string = a_dictionary.get(x)
        print("{}: {}".format(x, string))
