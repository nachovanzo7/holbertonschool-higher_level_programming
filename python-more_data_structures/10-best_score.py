#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if a_dictionary is None or not a_dictionary:
        return None
    max = max(a_dictionary, key=a_dictionary.get)
    return max
