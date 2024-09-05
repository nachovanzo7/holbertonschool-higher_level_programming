#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:  # Múltiplo de 3 y 5
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:  # Múltiplo de 3
            print("Fizz", end=" ")
        elif i % 5 == 0:  # Múltiplo de 5
            print("Buzz", end=" ")
        else:  # No es múltiplo de 3 ni de 5
            print(i, end=" ")
