# Python Exceptions

## Introducción

En Python, las excepciones son errores que ocurren durante la ejecución de un programa y que interrumpen el flujo normal de instrucciones. Las excepciones pueden ser provocadas por varios factores, como errores de entrada/salida, errores de programación o incluso condiciones inusuales en los datos.

### Conceptos Clave

- **Excepción**: Una interrupción del flujo normal del programa debido a un error.
- **Manejo de excepciones**: Proceso de "capturar" y manejar esos errores, evitando que el programa se detenga inesperadamente.
- **Bloques `try`, `except`, `else`, `finally`**: Estructuras que permiten gestionar excepciones.

## Manejo de Excepciones

Python ofrece varias formas de manejar excepciones mediante el uso de bloques `try` y `except`.

### Sintaxis Básica


try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre una excepción
    print("No se puede dividir entre cero")

    ## Bloques `else` y `finally`

- El bloque `else` se ejecuta si no ocurre ninguna excepción.
- El bloque `finally` se ejecuta siempre, ocurra o no una excepción, y es útil para realizar tareas de limpieza.


try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("No se puede dividir entre cero")
else:
    print("El resultado es:", resultado)
finally:
    print("Esta línea se ejecuta siempre")

    