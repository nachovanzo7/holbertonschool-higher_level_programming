#!/usr/bin/python3
def pow(a, b):
    sum = 1

    if b > 0:  
        for x in range(b):
            sum *= a
    elif b == 0:  
        return 1
    else:  
        for x in range(abs(b)):
            sum *= a
        sum = 1 / sum

    return sum
