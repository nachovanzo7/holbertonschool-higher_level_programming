# Aprendiendo Python: Condicionales, Bucles y Funciones

Este documento te proporcionará una guía básica para aprender los conceptos fundamentales de condicionales (`if/else`), bucles (`for` y `while`), y funciones en Python. Asegúrate de practicar con ejemplos y ejercicios para consolidar lo aprendido.

## 1. Condicionales: `if/else`

### Estructura básica

\```python
if condición:
    # Código a ejecutar si la condición es verdadera
elif otra_condición:
    # Código a ejecutar si la primera condición es falsa y otra_condición es verdadera
else:
    # Código a ejecutar si ninguna de las condiciones anteriores es verdadera
\```

### Ejemplo

\```python
x = 10

if x > 0:
    print("x es positivo")
elif x == 0:
    print("x es cero")
else:
    print("x es negativo")
\```

### Notas clave
- Los operadores de comparación comunes son: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- Puedes anidar múltiples `if/else` para verificar más de una condición.

## 2. Bucles

### `for`

Se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena).

\```python
for elemento in secuencia:
    # Código a ejecutar en cada iteración
\```

#### Ejemplo

\```python
for i in range(5):
    print(i)
\```

### `while`

Repite un bloque de código mientras una condición sea verdadera.

\```python
while condición:
    # Código a ejecutar mientras la condición sea verdadera
\```

#### Ejemplo

\```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
\```

### Notas clave
- `range(start, stop, step)` se utiliza comúnmente con `for` para generar una secuencia de números.
- Cuidado con los bucles infinitos al usar `while`; asegúrate de que la condición eventualmente se vuelva falsa.

## 3. Funciones

### Definición de una función

Las funciones permiten encapsular código en un bloque reutilizable.

\```python
def nombre_de_la_funcion(parámetros):
    # Código a ejecutar
    return resultado  # Opcional
\```

### Ejemplo

\```python
def suma(a, b):
    return a + b

resultado = suma(5, 3)
print(resultado)
\```

### Notas clave
- Usa `return` para devolver un valor desde la función. Si `return` no se especifica, la función devolverá `None`.
- Puedes definir funciones sin parámetros, con parámetros opcionales, o con un número variable de parámetros.

## 4. Ejercicios prácticos

### Condicionales
1. Escribe un programa que pida al usuario un número y determine si es par o impar.
2. Crea un programa que verifique si un año es bisiesto.

### Bucles
1. Crea un bucle que imprima los números del 1 al 10.
2. Escribe un bucle que recorra una lista de nombres y los imprima en mayúsculas.

### Funciones
1. Escribe una función que tome dos números y devuelva el mayor de ellos.
2. Crea una función que reciba una lista y devuelva la suma de sus elementos.

