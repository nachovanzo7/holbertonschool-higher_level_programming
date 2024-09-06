# Python Import & Modules

Este archivo describe el uso de importaciones y módulos en Python. Los módulos en Python son archivos que contienen definiciones y declaraciones de Python, los cuales se pueden reutilizar en otros scripts.

## Índice
1. [¿Qué es un Módulo?](#qué-es-un-módulo)
2. [Importar un Módulo](#importar-un-módulo)
3. [Importar Funciones o Variables Específicas](#importar-funciones-o-variables-específicas)
4. [Alias en Importaciones](#alias-en-importaciones)
5. [Módulos Personalizados](#módulos-personalizados)
6. [Módulos Integrados](#módulos-integrados)
7. [Ejemplos](#ejemplos)

## ¿Qué es un Módulo?

Un **módulo** es un archivo que contiene código de Python. Los módulos pueden definir funciones, clases y variables, y pueden incluir código ejecutable. Por ejemplo, puedes escribir tus funciones útiles en un archivo `.py` y reutilizarlas en otros scripts.

# modulo.py
def saludar():
    return "Hola, mundo"

# Importar un Módulo

Para importar un módulo en Python, se utiliza la palabra clave `import`. Al importar un módulo, puedes acceder a todas las funciones y variables definidas en ese archivo.

# main.py
import modulo

print(modulo.saludar())

# Importar Funciones o Variables Específicas

En lugar de importar todo el módulo, también puedes importar funciones o variables específicas usando la sintaxis `from ... import ...`.

# main.py
from modulo import saludar

print(saludar())

# Alias en Importaciones

Puedes dar un alias a los módulos o funciones que importas utilizando la palabra clave `as`.

# main.py
import modulo as m

print(m.saludar())

O puedes dar un alias a una función específica:

from modulo import saludar as saludo

print(saludo())

# Módulos Personalizados

Puedes crear tus propios módulos simplemente escribiendo código Python en archivos `.py`. Después, puedes importarlos en otros scripts para reutilizar el código.

# utilidades.py
def sumar(a, b):
    return a + b

Luego, puedes importar el módulo y utilizar la función `sumar` en otro archivo:

# main.py
import utilidades

resultado = utilidades.sumar(5, 3)
print(resultado)  # Salida: 8

# Módulos Integrados

Python viene con una gran cantidad de módulos integrados. Algunos de los más utilizados son:

- `math`: proporciona funciones matemáticas.
- `datetime`: maneja fechas y horas.
- `os`: permite interactuar con el sistema operativo.
- `random`: genera números aleatorios.