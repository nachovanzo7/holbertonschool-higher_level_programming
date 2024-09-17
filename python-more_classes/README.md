# `getattr()` función

El `getattr()` La función devuelve el valor del atributo especificado del objeto especificado.

## Sintaxis

getattr(objeto, atributo, por_defecto)

##Valores de Parametros

| Parámetro   | Descripción                                            |
|-------------|--------------------------------------------------------|
| objeto      | Requerido. Un objeto.                                  |
| atributo    | El nombre del atributo del que desea obtener el valor. |
| por_defecto | Opcional. El valor a devolver si el atributo no existe. |



# `__dict__` en Python

El atributo `__dict__` en Python es un diccionario que almacena todos los atributos (variables y métodos) de un objeto. Esto incluye tanto los atributos definidos por el usuario como los que son heredados de su clase. Cada objeto en Python que no sea un tipo básico (como enteros o cadenas) tiene su propio `__dict__`.

### ¿Cómo funciona?

Cuando creas un objeto o instancia de una clase, el atributo `__dict__` almacena toda la información relacionada con ese objeto en forma de pares clave-valor. La clave es el nombre del atributo y el valor es su contenido.

### Ejemplo simple:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Ana", 30)

# Acceder al diccionario de atributos
print(p.__dict__)

### Resultado:

```python
{'nombre': 'Ana', 'edad': 30}

