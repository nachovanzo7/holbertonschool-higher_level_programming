#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    if a_dictionary == None or not a_dictionary:
        return None
    i = max(a_dictionary, key=a_dictionary.get)
    return i
